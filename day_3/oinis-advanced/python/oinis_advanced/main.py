# -*- mode: python; python-indent: 4 -*-
import ncs
import _ncs
from ncs.dp import Action
from ncs.application import Service


# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------
class ServiceCallbacks(Service):

    # The create() callback is invoked inside NCS FASTMAP and
    # must always exist.
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info('Service create(service=', service._path, ')')

class ActionCallbacks(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info("ActionCallback: ", "cb_action")
    def cb_completion(self, uinfo, cli_style, token, completion_char,
                      kp, cmdpath, cmdparam_id, simpleType, extra):
        self.log.info("ActionCallback: ", "cb_completion({},{},{},{},{},{},{},{},{})".format(
            uinfo, cli_style, token, completion_char, kp, cmdpath, cmdparam_id, simpleType, extra))

        if_list = [(0, 'ge-0/1', None), (0, 'fe-0/0', None), (0, 'ge-0/2', None), (0, 'fe-0/66', None)]
        _ncs.dp.action_reply_completion(uinfo, if_list)

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
        self.register_service('oinis-advanced-servicepoint', ServiceCallbacks)
        self.register_action('if-action', ActionCallbacks)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
