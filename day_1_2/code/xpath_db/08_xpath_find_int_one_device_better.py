import ncs

device_name = "JUNIPER-1-NETSIM"
interface_find = "xe-"
xpath = "/devices/device[name='{}']/config/junos:configuration/interfaces/interface[starts-with(name,'{}')]"
device_path = xpath.format(device_name, interface_find )

def get_interfaces():
    inteface_list = []
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        def find_interface(kp, value):
            inteface_list.append(str(kp.dup()).split('interface{', 1)[1].rstrip('}'))
        read_trans.xpath_eval(device_path, find_interface, trace=None, path='')
    print(inteface_list)

get_interfaces()
