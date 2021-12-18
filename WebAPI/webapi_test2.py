import requests

import pytest

class test2():
  def test_metadata(self, hdrs, data):
     data = '{"path": "/Homework/math/f11.txt","include_media_info": false,"include_deleted": false,"include_has_explicit_shared_members": false}'
     return requests.post('https://api.dropboxapi.com/2/files/get_metadata', headers=headers, data=data)

# TEST2 data

headers = {
    'Authorization': 'Bearer pSqATe4TdSIAAAAAAAAAAb5gkfLSAhPdFCsg84SbsRO5WQT0Okn04UUMgWVv6D0a',
    'Content-Type': 'application/json',
}

data = '{"path": "/Homework/math/f11.txt","include_media_info": false,"include_deleted": false,"include_has_explicit_shared_members": false}'

response = requests.post('https://api.dropboxapi.com/2/files/get_metadata', headers=headers, data=data)

obj2 = test2();
response2 = obj2.test_metadata (headers,data);

print (response2.content)
assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAATQ", "client_modified": "2021-12-17T21:14:48Z", "server_modified": "2021-12-17T21:14:48Z", "rev": "5d35e076ad9888baf6171", "size": 326, "is_downloadable": true, "content_hash": "05fc3c7a8adc5c5a958350afaddab7ea8660c83dc2dbb436895f629e73201a30"}'




