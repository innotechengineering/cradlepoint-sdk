from time import sleep
from csclient import EventingCSClient

cp = EventingCSClient('connected_clients')
cp.log("1")
def update_desc(path, connected_clients, *args):
    mac_addresses = [client['mac'] for client in connected_clients]
    # mac_addresses = []
    # for client in connected_clients:
    #     if client['mac'] not in mac_addresses:
    #         mac_addresses.append(client['mac'])
    mac_addresses = ','.join(mac_addresses)
    cp.put('/config/system/desc', mac_addresses)

cp.register('put', '/status/lan/clients', update_desc)
