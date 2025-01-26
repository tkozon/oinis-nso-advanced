# Thread safe and NSO concurrent ready - handling conflicts
# -*- mode: python; python-indent: 4 -*-
import ncs
import _ncs
from ncs.application import Service
from ncs.dp import Action
import time
import random
PORT = 10022

# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------
class ServiceCallbacks(Service):

    # The create() callback is invoked inside NCS FASTMAP and
    # must always exist.

    @Service.pre_modification
    def cb_pre_modification(self, tctx, op, kp, root, proplist):
        if op != _ncs.dp.NCS_SERVICE_CREATE:
            return
        port_offset = self.get_data(root)
        # proplist hast to be added
        proplist.append(("port-offset", str(port_offset)))
        return proplist

    def get_data(self, root):
        port_offset = [None]
        maapi =ncs.maapi.Maapi()
        maapi.start_user_session('admin', "system")
        maapi.run_with_retry(lambda th:
                             self.get_data1(ncs.maagic.get_root(th), port_offset),
                             max_num_retries = 100)
        port_offset = port_offset[0]
        return port_offset

    def get_data1(self, root, res):
        port_offset = root["port-offset"]
        root["port-offset"] = port_offset + 1
        res[0] = port_offset
        return True

    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info('Service create(service=', service._path, ')')
        time.sleep(0.1)
        port_offset = int(proplist[0][1])
        vars = ncs.template.Variables()
        vars.add('DEVICE', 'device-' + service.name)
        vars.add('PORT', PORT + port_offset)
        template = ncs.template.Template(service)
        template.apply('device-template', vars)

    # The pre_modification() and post_modification() callbacks are optional,
    # and are invoked outside FASTMAP. pre_modification() is invoked before
    # create, update, or delete of the service, as indicated by the enum
    # ncs_service_operation op parameter. Conversely
    # post_modification() is invoked after create, update, or delete
    # of the service. These functions can be useful e.g. for
    # allocations that should be stored and existing also when the
    # service instance is removed.

    # @Service.pre_modification
    # def cb_pre_modification(self, tctx, op, kp, root, proplist):
    #     self.log.info('Service premod(service=', kp, ')')

    # @Service.post_modification
    # def cb_post_modification(self, tctx, op, kp, root, proplist):
    #     self.log.info('Service postmod(service=', kp, ')')



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
        self.register_service('concurrent-servicepoint', ServiceCallbacks)
        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
