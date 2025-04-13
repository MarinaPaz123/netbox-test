#!/usr/bin/python3

import pynetbox
URL = 'http://192.168.85.128/'
API_KEY = 'e89ec975b68720dc0ca9f2cab84f9ab546d4755e'
netbox = pynetbox.api(URL, token = API_KEY)

response_list = netbox.dcim.interfaces.filter(device='R1')
test_list = []
for i in response_list:
    test_list.append(i)
print(test_list)
