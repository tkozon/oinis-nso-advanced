import ncs
import time

def get_address():
    with ncs.maapi.single_read_trans("admin", "OINIS-READ") as read_trans:
        read_root = ncs.maagic.get_root(read_trans)
        address = read_root["devices"]["device"]["IOS-XR-1"]["address"]
        #time.sleep(15) - time sleep was added to show in the Context (OINIS-READ) in the NSO cli (who command)
        print(f"Address is : {address}")

get_address()
