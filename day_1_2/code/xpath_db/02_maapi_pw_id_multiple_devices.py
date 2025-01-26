import ncs

interface = "GigabitEthernet1/253"

def get_pw_id():
    pw_id_dict = {}
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        read_root = ncs.maagic.get_root(read_trans)
        devices = read_root["devices"]["device"]
        for device in devices:
            if device["platform"]["name"] == "ios-xr":
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
                                pw_ids = []
                                for n in neighbors:
                                    pw_ids.append(n['pw-id'])
                                    pw_id_dict[device.name] = pw_ids
                                        
    print(f"Device and PW-ID : {pw_id_dict}")
    
get_pw_id()
