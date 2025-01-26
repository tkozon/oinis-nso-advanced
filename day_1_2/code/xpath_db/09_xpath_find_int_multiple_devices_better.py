import ncs

interface_find = "xe-"
xpath = "/devices/device/config/junos:configuration/interfaces/interface[starts-with(name,'{}')]"
device_path = xpath.format(interface_find)

def get_interfaces():
    interface_dict = {}
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        def find_interface(kp, value):
            device_name = str(kp.dup()).split('device{')[1].split('}')[0]
            if device_name not in interface_dict:
                interface_dict[device_name] = []
            interface_dict[device_name].append(str(kp.dup()).split('interface{', 1)[1].rstrip('}'))
        read_trans.xpath_eval(device_path, find_interface, trace=None, path='')
    print(interface_dict)

get_interfaces()
