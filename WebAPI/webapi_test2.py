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
assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f111.txt", "path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAAEQ", "client_modified": "2021-12-15T23:21:12Z", "server_modified": "2021-12-15T23:21:12Z", "rev": "5d3378fcb3eb08baf6171", "size": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'




