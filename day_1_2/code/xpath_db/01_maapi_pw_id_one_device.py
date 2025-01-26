import ncs

device_name = "IOS-XR-1-NETSIM"
interface = "GigabitEthernet1/253"

def get_pw_id():
    pw_id_list=[]
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        read_root = ncs.maagic.get_root(read_trans)
        device = read_root["devices"]["device"][device_name]
        groups = device["config"]["l2vpn"]["xconnect"]["group"]
        for g in groups:
            group = groups[g["name"]]
            p2ps = group["p2p"]
            for p in group["p2p"]:
                p2p = p2ps[p["name"]]
                neighbors = p2p["neighbor"]
                interfaces = p2p["interface"]
                for i in interfaces:
                    if i["name"] == interface:
                        for n in neighbors:
                            pw_id_list.append((str(n['pw-id'])))
    print(f"List of PW-ID's : {pw_id_list}")

get_pw_id()
