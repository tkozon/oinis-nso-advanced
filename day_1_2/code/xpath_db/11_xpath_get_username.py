import ncs

xpath = "/aaa/authentication/users/user/name"

def get_usernames():
    with ncs.maapi.single_read_trans("admin", "system") as read_trans:
        def find_username(kp, value):
            print(f"Keypath : {kp}")
            print(f"Value : {value}")
        read_trans.xpath_eval(xpath, find_username, trace=None, path='')

get_usernames()
