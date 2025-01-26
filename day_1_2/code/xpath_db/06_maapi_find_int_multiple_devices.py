import ncs

interface_find = "xe-"

def get_interfaces():
    pw_id_dict = {}
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        read_root = ncs.maagic.get_root(read_trans)
        devices = read_root["devices"]["device"]
        for device in devices:
            if not device["platform"]["name"]:
                inteface_list = []
                for intf in device["config"]["configuration"]["interfaces"]["interface"]:
                    if intf["name"].startswith(interface_find):
                        inteface_list.append(intf["name"])
                    pw_id_dict[device["name"]] = inteface_list
    print(f"Device and PW-ID : {pw_id_dict}")

get_interfaces()
