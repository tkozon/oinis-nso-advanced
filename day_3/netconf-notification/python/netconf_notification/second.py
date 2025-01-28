# -*- mode: python; python-indent: 4 -*-
import ncs
import _ncs
import re
from ncs.dp import Action
from ncs.maapi import Maapi

class HandleNCConfigNotificationSecond(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info(f"Triggered {self.__class__.__name__}")
        self.log.info(f"KEYPATH : {kp} TYPE : {type(kp)}")
        self.log.info(f"============================")
        self.log.info(f"INPUT PATH : {input.path} TYPE : {type(input.path)}")
        self.log.info(f"============================")
        device_name = kp[1][0]
        self.log.info(f"DEVICE NAME : {device_name}")
        if input.tid is not None:
            with Maapi() as m:
                th = m.attach(input.tid)
                try:
                    notification = ncs.maagic.get_node(th, input.path)
                    changed_by = notification.changed_by
                    self.log.info(f"notif(username={changed_by.username}, session_id={changed_by.session_id}, source_host={changed_by.source_host})")
                    for edit in notification.edit:
                        self.log.info(f"edit(operation={edit.operation}, target={edit.target})")
                finally:
                    m.detach(input.tid)

# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):

    #pylint: disable=attribute-defined-outside-init
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('HandleNCConfigNotificationSecond RUNNING')
        self.register_action('handle-nc-config-notification-second', HandleNCConfigNotificationSecond)

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.
        self.log.info('HandleNCConfigNotificationSecond FINISHED')
