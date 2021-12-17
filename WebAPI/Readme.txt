
1. ��������� script_webapi.py �������� �� ����� Python. ��� ������� �������������� ����� PyCharm.
�������� ��� ��������� � �������� PyCharmProjects\pythonProject

��� ���������� pytest report ��������� ����������� ����� pytest -- ���������� �� Python ����� ������������, 
������� ������������ ��� ��������� � ���������� �������� �����.

��� ���������� Python behave ��������� ����������� ���������� behave c ������� ������� pip.
behave - �������� ��� ���������������� ��������� � python-�����.
Behave ���������� ����� ���������� �� ����������� �����, � ������� �� python.


2.��� ������� pytest report � ��������� ��������� ������� import pytest � assert

response = obj.test_upload (headers,data);
assert 'response.status_code == 200', 'Must be 200';

- �������� status code �������: ������ ���� 200

response2 = obj2.test_metadata (headers,data);
assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display":
 "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAAEQ", "client_modified": "2021-12-15T23:21:12Z",
 "server_modified": "2021-12-15T23:21:12Z", "rev": "5d3378fcb3eb08baf6171", "size": 343, "is_downloadable": true, 
"content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'

- �������� �������� ����������: ������ ��������� � ���������


���������� pytest:

�������:

============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\oleg\AppData\Local\Programs\Python\Python39\Scripts
collected 0 items

������:

============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\oleg\AppData\Local\Programs\Python\Python39\Scripts
collected 0 items / 1 error

=================================== ERRORS ====================================
__________________________ ERROR collecting main.py ___________________________
main.py:46: in <module>
    assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f111.txt", "path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAAEQ", "client_modified": "2021-12-15T23:21:12Z", "server_modified": "2021-12-15T23:21:12Z", "rev": "5d3378fcb3eb08baf6171", "size": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'
E   assert b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display": "/Homework/math/f11.txt"...ze": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}' == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f111.txt", "path_display": "/Homework/math/f11.txt...ze": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'
E    +  where b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display": "/Homework/math/f11.txt"...ze": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}' = <Response [200]>.content
------------------------------- Captured stdout -------------------------------
b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAAEQ", "client_modified": "2021-12-15T23:21:12Z", "server_modified": "2021-12-15T23:21:12Z", "rev": "5d3378fcb3eb08baf6171", "size": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'
=========================== short test summary info ===========================
ERROR main.py - assert b'{".tag": "file", "name": "f11.txt", "path_lower": "/...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 1.38s ===============================
=


3. ��� ������� ��������� �� ��������� ������ ����������� ���� script_wabapi.exe c ������� pyinstaller 
��������� �������� � �������� dist, ��� �� �������� ������� chromedriver.exe

pyinstaller script_webapi.py --noconsole --onefile

��������� ������������ ����� ��� ��������� � ����������� �����������.

4. � ��������� ��������� 3 ������ � ��������� ������� ���� ������� � ����� ����������� ����� ������� 

class test1()  - ���� �� ����������� �������� ����� (upload)

class test2() - ���� �� ����������� ��������� ���������� ����� (metadata)
  
class test3() - ���� �� ����������� �������� ����� (delete)

�����, ��������� ������� ������� � ���������� ������, ��������: 

obj = test1();
response = obj.test_upload (headers,data);

5. ��������� �������� ���������� ������������ �� �������� Python Behave. 
������ ������� /features c� ����������:
features
features/steps
� ������� features �������� ����� script_webapi.py , sc_web.feature
� ������� features/steps ������� ���� script_webapi_steps.py - c ������ �� ����������.

������ ������� ��� ������:

Feature: Response status code control # features/ft3.feature:1

  Scenario: Make request and check the status code of it  # features/ft3.feature:2
    Given a Site                                          # features/steps/ft3.py:4
    When the request is run                               # features/steps/ft3.py:7
    Then the Site returns status code of request          # features/steps/ft3.py:23

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.236s

������ �������� � ���� �����:
script_webapi.py - �������� ������
script_webapi_steps.py - ���� c ������ �� ����������
sc_st.feature - ���� �������� ����������
script_webapi.exe - ����������� ���� �� ��������

