
1. Комплекс из 3-х тестов webapi_test1.py, webapi_test2.py, webapi_test3.py написаны на языке Python. 

webapi_test1.py  - тест по результатам загрузки файла (upload)
webapi_test2.py  - тест по результатам получения метаданных файла (metadata)
webapi_test3.py - тест по результатам удаления файла (delete)

Для запуска использовалась среда PyCharm.
Исходный код находится в каталоге PyCharmProjects\pythonProject

Для реализации pytest report выполнена инсталляция среды pytest -- основанная на Python среда тестирования, 
которая используется для написания и выполнения тестовых кодов.

Для реализации Python behave выполнена инсталляция приложения behave c помощью команды pip.
behave - фрейморк для программирования поведения в python-стиле.
Behave использует тесты написанные на натуральном языке, с логикой на python.

2.Для запуска pytest report в программу добавлены команды import pytest и assert

Например: 
- проверка status code сервера: должен быть 200
response = obj.test_upload (headers,data);
assert 'response.status_code == 200', 'Must be 200';

- проверка контента метаданных: должны совпадать с заданными (могут изменяться со временем, тогда будет выдаваться ошибка)
response2 = obj2.test_metadata (headers,data);
assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", 
"path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAATQ", "client_modified": "2021-12-17T21:14:48Z",
"server_modified": "2021-12-17T21:14:48Z", "rev": "5d35e076ad9888baf6171", "size": 326, "is_downloadable": true, "content_hash": "05fc3c7a8adc5c5a958350afaddab7ea8660c83dc2dbb436895f629e73201a30"}'


Результаты pytest:

Успешно:

============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\oleg\AppData\Local\Programs\Python\Python39\Scripts
collected 0 items

Ошибка:

platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\vadmu\AppData\Local\Programs\Python\Python39\Scripts
collected 0 items / 1 error

=================================== ERRORS ====================================
__________________________ ERROR collecting main.py ___________________________
main.py:47: in <module>
    assert response2.content == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f111.txt", "path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAAEQ", "client_modified": "2021-12-15T23:21:12Z", "server_modified": "2021-12-15T23:21:12Z", "rev": "5d3378fcb3eb08baf6171", "size": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'
E   assert b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display": "/Homework/math/f11.txt"...ze": 326, "is_downloadable": true, "content_hash": "05fc3c7a8adc5c5a958350afaddab7ea8660c83dc2dbb436895f629e73201a30"}' == b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f111.txt", "path_display": "/Homework/math/f11.txt...ze": 343, "is_downloadable": true, "content_hash": "f5ac58d397a8e2a81080a2ffea4559b63754596d2305d72506184b372133f448"}'
E    +  where b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display": "/Homework/math/f11.txt"...ze": 326, "is_downloadable": true, "content_hash": "05fc3c7a8adc5c5a958350afaddab7ea8660c83dc2dbb436895f629e73201a30"}' = <Response [200]>.content
------------------------------- Captured stdout -------------------------------
b'{".tag": "file", "name": "f11.txt", "path_lower": "/homework/math/f11.txt", "path_display": "/Homework/math/f11.txt", "id": "id:iG-4id_7ykkAAAAAAAAATQ", "client_modified": "2021-12-17T21:14:48Z", "server_modified": "2021-12-17T21:14:48Z", "rev": "5d35e076ad9888baf6171", "size": 326, "is_downloadable": true, "content_hash": "05fc3c7a8adc5c5a958350afaddab7ea8660c83dc2dbb436895f629e73201a30"}'
=========================== short test summary info ===========================
ERROR main.py - assert b'{".tag": "file", "name": "f11.txt", "path_lower": "/...
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 1.70s ===============================

3. Для запуска программы из командной строки скоплирован файлы webapi_test1.exe, webapi_test2.exe, webapi_test3.exe 
c помощью pyinstaller 

pyinstaller webapi_test1.py --onefile
pyinstaller webapi_test2.py --onefile
pyinstaller webapi_test3.py --onefile

4. В каждой из программ объявлено по 1 классу, создаются объекты этих классов и далее выполняется вызов методов 

webapi_test1.py:  class test1()  - тест по результатам загрузки файла (upload)

webapi_test2.py:  class test2() - тест по результатам получения метаданных файла (metadata)
  
webapi_test3.py:  class test3() - тест по результатам удаления файла (delete)

Далее, создаются объекты классов и вызываются методы, например: 

obj = test1();
response = obj.test_upload (headers,data);

5. Добавлены средства реализации тестирования по сценарию Python Behave для теста 1 - webapi_test1.py
Создан каталог /features cо структурой:
features
features/steps
в каталог features записаны файлы script_webapi.py , sc_web.feature
в каталог features/steps записан файл script_webapi_steps.py - c шагами по тестировке.

Пример запуска без ошибок:

Feature: Response status code control # features/ft3.feature:1

  Scenario: Make request and check the status code of it  # features/sc_web.feature:2
    Given a Site                                          # features/steps/script_webapi_steps.py:4
    When the request is run                               # features/steps/script_webapi_steps.py:7
    Then the Site returns status code of request          # features/steps/script_webapi_steps.py:23

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.236s

Проект включает в себя файлы:
webapi_test1.py, webapi_test2.py, webapi_test3.py  - скрипты с тестами 1, 2 и 3
script_webapi_steps.py - файл c шагами по тестировке
sc_web.feature - файл сценария тестировки
webapi_test1.exe, webapi_test2.exe, webapi_test3.exe - исполняемый файл со скриптом

