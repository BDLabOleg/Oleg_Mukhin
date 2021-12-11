import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElement():
  def find_type(self, s1, s2):
     return driver.find_element(By.NAME,s1).send_keys(s2);

class FindClickbyname():
  def find_click(self,s1):
      return driver.find_element(By.NAME,s1).click();

class FindClickbyID():
  def find_click(self,s1):
      return driver.find_element(By.ID,s1).click();

driver = webdriver.Chrome();
driver.get('https://opensource-demo.orangehrmlive.com/login');

obj = FindElement();

s1='txtUsername';  s2='Admin';
assert s2=='Admin', 'Must be Admin';

obj.find_type(s1,s2);

s1='txtPassword';  s2='admin123';
assert s2=='admin123', 'Wrong Password';
obj.find_type(s1, s2);

obj2 = FindClickbyname();

s1='Submit';
obj2.find_click(s1);

driver.get('https://opensource-demo.orangehrmlive.com/index.php/admin/workShift')

s1='btnAdd';
obj2.find_click(s1);

s1='workShift[name]';  s2='RandomName';
obj.find_type(s1,s2);

s1='workShift[workHours][from]';  s2='08:00';
assert s2 >= '06:00', 'Wrong time'
obj.find_type(s1,s2);

s1='workShift[workHours][to]';  s2='16:00';
assert s2 <= '18:00', 'Wrong time'
obj.find_type(s1,s2);

s1='workShift[availableEmp][]';  s2='RandomName';
obj.find_type(s1,s2);

obj3 = FindClickbyID();

s1='btnAssignEmployee';
obj3.find_click(s1);

s1='btnSave';
obj3.find_click(s1); 