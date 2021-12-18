
import requests

import pytest

class test3():
    def test_delete(self, hdrs, data):
       return requests.post('https://api.dropboxapi.com/2/files/delete_v2', headers=headers, data=data)

# TEST3 data

headers = {
    'Authorization': 'Bearer sl.A-S5uEfU_9T68kOS7YyDNk6UdxvvsrpbtDH9FOb511-95NoiMkb2oUpQxMJVb5YjBk77PftcGztX7atOLGIme6YdCEoyEFjv_Odo_7qI07qZmtNUvcvzNH6JvjmOQ6cIrJLak0NuaB0K',
    'Content-Type': 'application/json',
}

data = '{"path": "/Homework/math/cinema.iml"}'

response = requests.post('https://api.dropboxapi.com/2/files/delete_v2', headers=headers, data=data)

obj3 = test3();
response3 = obj3.test_delete (headers,data);

print (response3.status_code)
assert response3.status_code == 401