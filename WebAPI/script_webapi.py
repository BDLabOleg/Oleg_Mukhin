import requests

# import pytest

class test1():
  def test_upload(self, hdrs, data):
  #   data = open('c://Users/vadmu/cinema.iml', 'rb').read()
      data = open('Readme.txt', 'rb').read()
      return requests.post('https://content.dropboxapi.com/2/files/upload', headers=headers, data=data)

class test2():
  def test_metadata(self, hdrs, data):
     data = '{"path": "/Homework/math/f11.txt","include_media_info": false,"include_deleted": false,"include_has_explicit_shared_members": false}'
     return requests.post('https://api.dropboxapi.com/2/files/get_metadata', headers=headers, data=data)

class test3():
    def test_delete(self, hdrs, data):
       return requests.post('https://api.dropboxapi.com/2/files/delete_v2', headers=headers, data=data)

# TEST1 data
headers = {
    'Authorization': 'Bearer pSqATe4TdSIAAAAAAAAAAb5gkfLSAhPdFCsg84SbsRO5WQT0Okn04UUMgWVv6D0a',
    'Dropbox-API-Arg': '{"path": "/Homework/math/f11.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
    'Content-Type': 'application/octet-stream',
}

# data = open('c://Users/vadmu/cinema.iml', 'rb').read()

# obj = test1();
# response = obj.test_upload (headers,data);
# assert 'response.status_code == 200', 'Must be 200';

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
# assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f111.txt", "path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAAEQ", "client_modified": "2021-12-15T23:21:12Z", "server_modified": "2021-12-15T23:21:12Z", "rev": "5d3378fcb3eb08baf6171", "size": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'


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
# assert response3.status_code == 401


