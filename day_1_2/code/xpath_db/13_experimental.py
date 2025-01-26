import ncs
from ncs.experimental import Query

vrf = "OINIS-VRF"
device = "IOS-XR-1-NETSIM"
path = "/devices/device[name='{}']/config/cisco-ios-xr:vrf/vrf-list[name='{}']"
vrf_path = path.format(device, vrf)

def get_vrf():
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        with Query(read_trans, vrf_path, '/', ["rd", "vpn", "fallback-vrf",], result_as=ncs.QUERY_STRING) as query:
            for result in query:
                print(result)

get_vrf()
