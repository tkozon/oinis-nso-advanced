import ncs

device_name = "JUNIPER-1-NETSIM"
interface_find = "xe-"

def get_interfaces():
    inteface_list = []
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        read_root = ncs.maagic.get_root(read_trans)
        device = read_root["devices"]["device"][device_name]
        for intf in device["config"]["configuration"]["interfaces"]["interface"]:
            if intf["name"].startswith(interface_find):
                inteface_list.append(intf["name"])
    print(f"List of Interfaces : {inteface_list}")

get_interfaces()
