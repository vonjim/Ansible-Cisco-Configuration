
'''
   A module that recevies the device type (Router/Switch) sets the source interface to loopback0 if it is a router or SVI if switch

'''
device_types = {'Router': 'loopback0', 'Switch': 'vlan 5'}

return device_type[device] 

