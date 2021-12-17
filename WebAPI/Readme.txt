
1. Программа script_webapi.py написана на языке Python. Для запуска использовалась среда PyCharm.
Исходный код находится в каталоге PyCharmProjects\pythonProject

Для реализации pytest report выполнена инсталляция среды pytest -- основанная на Python среда тестирования, 
которая используется для написания и выполнения тестовых кодов.

Для реализации Python behave выполнена инсталляция приложения behave c помощью команды pip.
behave - фрейморк для программирования поведения в python-стиле.
Behave использует тесты написанные на натуральном языке, с логикой на python.


2.Для запуска pytest report в программу добавлены команды import pytest и assert

response = obj.test_upload (headers,data);
assert 'response.status_code == 200', 'Must be 200';

- проверка status code сервера: должен быть 200

response2 = obj2.test_metadata (headers,data);
assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display":
 "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAAEQ", "client_modified": "2021-12-15T23:21:12Z",
 "server_modified": "2021-12-15T23:21:12Z", "rev": "5d3378fcb3eb08baf6171", "size": 343, "is_downloadable": true, 
"content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'

- проверка контента метаданных: должны совпадать с заданными


Результаты pytest:

Успешно:

============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\oleg\AppData\Local\Programs\Python\Python39\Scripts
collected 0 items

Ошибка:

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


3. Для запуска программы из командной строки скоплирован файл script_wabapi.exe c помощью pyinstaller 
Программа хранится в каталоге dist, там же хранится драйвер chromedriver.exe

pyinstaller script_webapi.py --noconsole --onefile

генерация исполняемого файла для программы с графическим интерфейсом.

4. В программе объявлены 3 класса и создаются объекты этих классов и далее выполняется вызов методов 

class test1()  - тест по результатам загрузки файла (upload)

class test2() - тест по результатам получения метаданных файла (metadata)
  
class test3() - тест по результатам удаления файла (delete)

Далее, создаются объекты классов и вызываются методы, например: 

obj = test1();
response = obj.test_upload (headers,data);

5. Добавлены средства реализации тестирования по сценарию Python Behave. 
Создан каталог /features cо структурой:
features
features/steps
в каталог features записаны файлы script_webapi.py , sc_web.feature
в каталог features/steps записан файл script_webapi_steps.py - c шагами по тестировке.

Пример запуска без ошибок:

Feature: Response status code control # features/ft3.feature:1

  Scenario: Make request and check the status code of it  # features/ft3.feature:2
    Given a Site                                          # features/steps/ft3.py:4
    When the request is run                               # features/steps/ft3.py:7
    Then the Site returns status code of request          # features/steps/ft3.py:23

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.236s

Проект включает в себя файлы:
script_webapi.py - основной скрипт
script_webapi_steps.py - файл c шагами по тестировке
sc_st.feature - файл сценария тестировки
script_webapi.exe - исполняемый файл со скриптом

