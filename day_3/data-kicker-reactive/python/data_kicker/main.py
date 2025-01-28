# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service, PlanComponent
from ncs.dp import Action
from resource_manager import id_allocator
import ncs.maagic as maagic
import ncs.maapi as maapi
import time
# ------------------------
# SERVICE CALLBACK EXAMPLE
# ------------------------


class DeletePlanAction(Action):
    """
    Implements the delete-plan action. This class is bound to the
    'delete-plan-actionpoint' actionpoint defined in YANG.
    """
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output):
        self.log.info(f"delete-plan action invoked for path: {kp}")
        maap = ncs.maapi.Maapi()
        with ncs.maapi.Maapi() as m:
            with ncs.maapi.Session(m, 'admin', 'system'):
                with m.start_write_trans() as write_trans:
                    read_root = ncs.maagic.get_root(write_trans)
                    del read_root.data_kicker__plan_data
                    write_trans.apply()


class ServiceCallbacks(Service):
    # The create() callback is invoked inside NCS FASTMAP and
    # must always exist.
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        template = ncs.template.Template(service)
        service_path = f'/data-kicker:data-kicker-service[name={service.name}]'
        id_allocator.id_request(service, service_path, tctx.username, 'SERVICE', service.name,  False)
        service_alloc_id = id_allocator.id_read(tctx.username, root, 'SERVICE', service.name)
        if service_alloc_id is None:
            self.log.info('Service create(service=', service._path, ')')
            self.log.info(f'Allocation is not ready yet. Redeploying ....')
            template.apply("data-kicker")
            return
        if not self.is_init_plan_reached(root):
            self.log.info("Service does not have ncs:init status reached yet")
        elif self.is_init_plan_reached(root) and not self.is_ready_plan_reached(root):
            self.log.info(f"ncs:init status reached but ncs:ready not reached")
            service.test1 = "test1"
            template.apply("data-kicker")
            return
        elif self.is_init_plan_reached(root) and self.is_ready_plan_reached(root):
            self.log.info(f"ncs:init status reached and ncs:readyreached")
            service.test2 = "test2"
            return

    def is_init_plan_reached(self, root):
        try:
            return root.data_kicker__plan_data.plan["TEST"].plan.component['self'].state['ncs:init'].status == "reached"
        except KeyError:
            return False

    def is_ready_plan_reached(self, root):
        try:
            return root.data_kicker__plan_data.plan["TEST"].plan.component['self'].state['ncs:ready'].status == "reached"
        except KeyError:
            return False
    
class KickerActionOutside(Action):
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output, trans):
        self.log.info(f"Triggered {self.__class__.__name__}")
        self.log.info(f"KP {kp}")
        self.log.info(f"PATH {input.path}")
        with maapi.single_write_trans(uinfo.username, uinfo.context, db=ncs.RUNNING) as th:
            root = maagic.get_root(th)
            if not self.is_init_plan_reached(root):
                plan_entry = root.data_kicker__plan_data.plan.create("TEST")
                # 2. Construct a PlanComponent around that plan entry, not around the service node
                plan = PlanComponent(plan_entry, "self", "ncs:self")
                plan.append_state("ncs:init")
                plan.append_state("data-kicker:applying-vm-config")
                plan.append_state("data-kicker:allocation")
                plan.append_state("ncs:ready")
                plan.set_reached("ncs:init")
                th.apply()
        with maapi.single_read_trans(uinfo.username, uinfo.context, db=ncs.RUNNING) as th:
            root = maagic.get_root(th)
            if not self.is_init_plan_reached(root):
                service = root.data_kicker_service["TEST"]
                time.sleep(15)
                # If no inputs are needed, just call it:
                service.reactive_re_deploy()
            if self.is_init_plan_reached(root) and not self.is_ready_plan_reached(root):
                service = root.data_kicker_service["TEST"]
                time.sleep(15)
                with maapi.single_write_trans(uinfo.username, uinfo.context, db=ncs.RUNNING) as write_th:
                    write_root = maagic.get_root(write_th)
                    plan_entry = write_root.data_kicker__plan_data.plan.create("TEST")
                    plan = PlanComponent(plan_entry, "self", "ncs:self")
                    plan.set_reached("ncs:ready")
                    write_th.apply()
                # If no inputs are needed, just call it:
                service.reactive_re_deploy()

    def is_init_plan_reached(self, root):
        try:
            return root.data_kicker__plan_data.plan["TEST"].plan.component['self'].state['ncs:init'].status == "reached"
        except KeyError:
            return False
    
    def is_ready_plan_reached(self, root):
        try:
            return root.data_kicker__plan_data.plan["TEST"].plan.component['self'].state['ncs:ready'].status == "reached"
        except KeyError:
            return False
        
   

    

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
        self.register_action('reactive-re-deploy-action', KickerActionOutside)
        self.register_action('delete-plan-actionpoint', DeletePlanAction)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
