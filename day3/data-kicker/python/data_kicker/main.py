# -*- mode: python; python-indent: 4 -*-
import ncs
import _ncs
from ncs.application import Service
from ncs.dp import Action
from ncs.maapi import Maapi
# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------
class ServiceCallbacks(Service):

    # The create() callback is invoked inside NCS FASTMAP and
    # must always exist.
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info('Service create(service=', service._path, ')')

class KickerAction(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info(f"Triggered {self.__class__.__name__}")
        self.log.info(f"PATH {input.path}")
        if input.tid is not None:
            try:
                with ncs.maapi.Maapi() as m:
                    with m.attach(input.tid, 0) as t:
                        service = ncs.maagic.get_node(t, input.path)
                        self.log.info(f" BW is : {service.bw}")
                        diter = ServiceOpDiffIterator(input.path, self.log)
                        t.diff_iterate(diter, 0)
                        self.log.info('Service operation - ', diter.op)

            except Exception as error:
                self.log.error(f"Exception while processing KickerAction: {str(error)} ")

class KickerActionOutside(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info(f"Triggered {self.__class__.__name__}")
        self.log.info(f"PATH {input.path}")
        if input.tid is not None:
            try:
                with ncs.maapi.Maapi() as m:
                    with m.attach(input.tid, 0) as t:
                        diter = ServiceOpDiffIterator(input.path, self.log)
                        t.diff_iterate(diter, 0)
                        self.log.info('Service operation - ', diter.op)
                        if diter.op != "deleted":
                            service = ncs.maagic.get_node(t, input.path)
                            self.log.info(f" BW is : {service.bw}")

            except Exception as error:
                self.log.error(f"Exception while processing KickerAction: {str(error)} ")

class ServiceOpDiffIterator(object):
    def __init__(self, path, log):
        self.op = "modified"
        self.path = path
        self.log = log

    def __call__(self, keypath, op, oldv, newv):
        self.log.info (f"diff iter params {keypath}, {op}, {oldv}, {newv}")
        if str(self.path) == str(keypath):
            if op == _ncs.MOP_DELETED:
                self.op = "deleted"
            elif op == _ncs.MOP_CREATED:
                self.op = "created"
        return ncs.ITER_STOP

# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('Main RUNNING')

        # Service callbacks require a registration for a 'service point',
        # as specified in the corresponding data model.
        #
        self.register_service('data-kicker-servicepoint', ServiceCallbacks)
        self.register_action('log-action', KickerAction)
        self.register_action('log-action-outside', KickerActionOutside)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
