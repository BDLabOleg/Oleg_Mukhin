import requests

import pytest

class test1():
  def test_upload(self, hdrs, data):
      data = open('Readme.txt', 'rb').read()
      return requests.post('https://content.dropboxapi.com/2/files/upload', headers=headers, data=data)

data = open('Readme.txt', 'rb').read()

# TEST1 data
headers = {
    'Authorization': 'Bearer pSqATe4TdSIAAAAAAAAAAb5gkfLSAhPdFCsg84SbsRO5WQT0Okn04UUMgWVv6D0a',
    'Dropbox-API-Arg': '{"path": "/Homework/math/f11.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
    'Content-Type': 'application/octet-stream',
}

obj = test1();
response = obj.test_upload (headers,data);
assert 'response.status_code == 200', 'Must be 200';
