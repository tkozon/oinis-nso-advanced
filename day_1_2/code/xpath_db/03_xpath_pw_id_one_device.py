import ncs

device_name = "IOS-XR-1-NETSIM"
interface = "GigabitEthernet1/253"
xpath = "/devices/device[name='{}']/config/cisco-ios-xr:l2vpn/xconnect/group/p2p/interface[name='{}']"
device_path = xpath.format(device_name, interface)

def get_pw_id():
    pw_id_list=[]
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        def find_interface(kp, value):
            # Remove interface from keypath
            p2p_node = ncs.maagic.get_node(read_trans, str(kp).split("interface{")[0])
            for neighbor in p2p_node["neighbor"]:
                pw_id_list.append(neighbor["pw-id"])
        read_trans.xpath_eval(device_path, find_interface, trace=None, path='')
    print(f"List of PW-ID's : {pw_id_list}")

get_pw_id()
