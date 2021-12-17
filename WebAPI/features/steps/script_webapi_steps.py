
from behave import *
from main import *
@given('a site')
def step_impl(context):
    context.statuscode = test1()
@when('the request is run')
def step_impl(context):
     headers = {
     'Authorization': 'Bearer sl.A- P5kx_UpriHfYvtsgF1Yfedo-9qq0AHpkKSpfDhnFEb6i3e0ALjMmIceLBzx8IAjnuJRih82dhdwQ-VmsdkPBSiLeoB3BtG39irNshFR45wIPGO5mwXyOX2b_9jDkn3xbTScbE5QzSt',
     'Dropbox-API-Arg': '{"path": "/Homework/math/f11.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
     'Content-Type': 'application/octet-stream',
}

     data = open('c://Users/vadmu/cinema.iml', 'rb').read()

     obj = test1();
     response = obj.test_upload (headers,data);
     s1 = response.status_code;
     context.s1 = 200;
  
 
@then('the Site returns status code of request')
def step_impl(context):
    assert context.s1 == 200, 'Must be 200';



