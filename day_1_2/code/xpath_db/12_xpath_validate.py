import ncs

device_name = "IOS-XR-1-NETSIM"
interface = "GigabitEthernet1/253"
xpath = "/devices/device[name='{}']/config/cisco-ios-xr:l2vpn/xconnect/group/p2p/interface[name='{}']"
device_path = xpath.format(device_name, interface)

def validate_data():
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        print(read_trans.xpath_eval_expr(device_path, trace=None, path=''))

validate_data()
