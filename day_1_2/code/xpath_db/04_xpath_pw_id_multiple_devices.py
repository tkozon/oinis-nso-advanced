import ncs

interface = "GigabitEthernet1/253"
xpath = "/devices/device/config/cisco-ios-xr:l2vpn/xconnect/group/p2p/interface[name='{}']"
device_path = xpath.format(interface)

def get_pw_id():
    pw_id_dict = {}
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        def find_interface(kp, value):
            pw_id_list = []
            # Remove config from keypath
            device = ncs.maagic.get_node(read_trans, str(kp).split("config/")[0])
            # Remove interface from keypath
            p2p_node = ncs.maagic.get_node(read_trans, str(kp).split("interface{")[0])
            for neighbor in p2p_node["neighbor"]:
                pw_id_list.append(neighbor["pw-id"])
                pw_id_dict[device["name"]] = pw_id_list
        read_trans.xpath_eval(device_path, find_interface, trace=None, path='')
    print(f"Device and PW-ID : {pw_id_dict}")

get_pw_id()
