import ncs

vrf = "OINIS-VRF"
device = "IOS-XR-1-NETSIM"
path = "/devices/device[name='{}']/config/cisco-ios-xr:vrf/vrf-list[name='{}']"
vrf_path = path.format(device, vrf)

def get_vrf():
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        maapi = read_trans.maapi
        select = ["rd", "vpn", "fallback-vrf",]
        initial_offset = 0
        query = maapi.query_start(
            read_trans.th, expr=vrf_path, context_node="/",
            chunk_size=0, initial_offset=initial_offset,
            result_as=ncs.QUERY_STRING, select=select, sort=[]
        )
        total_result = maapi.query_result_count(query)
        query_result = maapi.query_result(query)
        response = [item for sublist in query_result for item in sublist]
    print(f"Total result : {total_result}")
    print(response)

get_vrf()
