
1. ��������� script_site �������� �� ����� Python. ��� ������� �������������� ����� PyCharm.
�������� ��� ��������� � �������� PyCharmProjects\pythonProject
���������� selenium - ���������� ��� ������������� �������� ���-��������.

� ������� PyCharmProjects\pythonProject �������� ���� � ��������� chromedriver.exe - �������� �� ���������� 
Chrome � ������� ������� ������������

��� ���������� pytest report ��������� ����������� ����� pytest -- ���������� �� Python ����� ������������, 
������� ������������ ��� ��������� � ���������� �������� �����.

��� ���������� Python behave ��������� ����������� ���������� behave c ������� ������� pip.
behave - �������� ��� ���������������� ��������� � python-�����.
Behave ���������� ����� ���������� �� ����������� �����, � ������� �� python.


2.��� ������� pytest report � ��������� ��������� ������� import pytest � assert �� ���� ����������, 
����� ��� �������� ����� login password � ������� ������ ���������� - �� ����� 06:00 � �� ������� 18:00

assert s2=='Admin', 'Must be Admin';

assert s2=='admin123', 'Wrong Password';

assert s2 >= '06:00', 'Wrong time'

assert s2 <= '18:00', 'Wrong time'

���������� pytest:

�������:
============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\oleg\AppData\Local\Application Data\Programs\Python\Python39\Scripts
collected 0 items


������:
============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\oleg\AppData\Local\Application Data\Programs\Python\Python39\Scripts
collected 0 items / 1 error

=================================== ERRORS ====================================
__________________________ ERROR collecting script_site.py ___________________________
main.py:34: in <module>
    assert s2=='admin123', 'Wrong Password';
E   AssertionError: Wrong Password
E   assert 'admin122' == 'admin123'
=========================== short test summary info ===========================
ERROR main.py - AssertionError: Wrong Password
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 3.41s ===============================


3. ��� ������� ��������� �� ��������� ������ ����������� ���� script_site.exe c ������� pyinstaller 
��������� �������� � �������� dist, ��� �� �������� ������� chromedriver.exe

pyinstaller script_site.py --noconsole --onefile

��������� ������������ ����� ��� ��������� � ����������� �����������.

4. � ��������� ��������� 3 ������ � ��������� ������� ���� ������� � ����� ����������� ����� ������� 

class FindElement()  - ����� �������� �� �����

class FindClickbyname() - ����� �������� �� ����� � �������� �������
  
class FindClickbyID() - ����� �������� �� ID � �������� �������

�����, ��������� ������� ������� � ���������� ������, ��������: 

   obj = FindElement();
   s1='txtUsername';  s2='Admin';
   assert s2=='Admin', 'Must be Admin';
   obj.find_type(s1,s2);

5. ��������� �������� ���������� ������������ �� �������� Python Behave. 
������ ������� /features c� ����������:
features
features/steps
� ������� features �������� ����� script_site.py , sc_st.feature
� ������� features/steps ������� ���� script_site_steps.py - c ������ �� ����������.

������ ������� ��� ������:
Feature: The Login to site # features/sc_st.feature:1

  Scenario: Enter the login (Admin)      # features/sc_st.feature:2
    Given a Site                         # features/steps/script_site_steps.py:5
    When the login starts                # features/steps/script_site_steps.py:8
    Then the User must enter login Admin # features/steps/script_site_steps.py:17

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m5.437s


������ ������� ��� ������� ������:

� ����� ������� �������� ������ s2='Admil' (������ ���� 'Admin')

s1='txtUsername';  s2='Admil';
assert s2=='Admin', 'Must be Admin';
obj.find_type(s1,s2);

����� ���������� ������������:
Exception AssertionError: Must be Admin
 Then the User must enter login Admin # features/steps/script_site_steps.py:17               


������ �������� � ���� �����:
script_site.py - �������� ������
script_site_steps.py - ���� c ������ �� ����������
sc_st.feature - ���� �������� ����������
script_site.exe - ����������� ���� �� ��������

����� ��������� ��������� �������� chromedriver.exe � ������� ��������


