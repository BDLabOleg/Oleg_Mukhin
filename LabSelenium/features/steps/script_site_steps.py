
from behave import *
from main import *
@given('a site')
def step_impl(context):
    context.findelement = FindElement()
@when('the login starts')
def step_impl(context):
     driver = webdriver.Chrome();
     driver.get('https://opensource-demo.orangehrmlive.com/login');
     obj = FindElement();
     s1='txtUsername';
     context.s2='Admin';
   
@then('the user must enter login Admin')
def step_impl(context):
    assert context.s2=='Admin',' Must be  Admin';

