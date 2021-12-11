
1. Программа script_site написана на языке Python. Для запуска использовалась среда PyCharm.
Исходный код находится в каталоге PyCharmProjects\pythonProject
Установлен selenium - инструмент для автоматизации действий веб-браузера.

В каталог PyCharmProjects\pythonProject добавлен файл с драйвером chromedriver.exe - отвечает за управление 
Chrome с помощью внешних инструментов

Для реализации pytest report выполнена инсталляция среды pytest -- основанная на Python среда тестирования, 
которая используется для написания и выполнения тестовых кодов.

Для реализации Python behave выполнена инсталляция приложения behave c помощью команды pip.
behave - фрейморк для программирования поведения в python-стиле.
Behave использует тесты написанные на натуральном языке, с логикой на python.


2.Для запуска pytest report в программу добавлены команды import pytest и assert по ряду параметров, 
таких как контроль ввода login password и времени работы сотрудника - не ранее 06:00 и не позднее 18:00

assert s2=='Admin', 'Must be Admin';

assert s2=='admin123', 'Wrong Password';

assert s2 >= '06:00', 'Wrong time'

assert s2 <= '18:00', 'Wrong time'

Результаты pytest:

Успешно:
============================= test session starts =============================
platform win32 -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\oleg\AppData\Local\Application Data\Programs\Python\Python39\Scripts
collected 0 items


Ошибка:
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


3. Для запуска программы из командной строки скоплирован файл script_site.exe c помощью pyinstaller 
Программа хранится в каталоге dist, там же хранится драйвер chromedriver.exe

pyinstaller script_site.py --noconsole --onefile

генерация исполняемого файла для программы с графическим интерфейсом.

4. В программе объявлены 3 класса и создаются объекты этих классов и далее выполняется вызов методов 

class FindElement()  - поиск элемента по имени

class FindClickbyname() - поиск элемента по имени с нажатием клавиши
  
class FindClickbyID() - поиск элемента по ID с нажатием клавиши

Далее, создаются объекты классов и вызываются методы, например: 

   obj = FindElement();
   s1='txtUsername';  s2='Admin';
   assert s2=='Admin', 'Must be Admin';
   obj.find_type(s1,s2);

5. Добавлены средства реализации тестирования по сценарию Python Behave. 
Создан каталог /features cо структурой:
features
features/steps
в каталог features записаны файлы script_site.py , sc_st.feature
в каталог features/steps записан файл script_site_steps.py - c шагами по тестировке.

Пример запуска без ошибок:
Feature: The Login to site # features/sc_st.feature:1

  Scenario: Enter the login (Admin)      # features/sc_st.feature:2
    Given a Site                         # features/steps/script_site_steps.py:5
    When the login starts                # features/steps/script_site_steps.py:8
    Then the User must enter login Admin # features/steps/script_site_steps.py:17

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m5.437s


Пример запуска при наличии ошибки:

В файле скрипта допущена ошибка s2='Admil' (должно быть 'Admin')

s1='txtUsername';  s2='Admil';
assert s2=='Admin', 'Must be Admin';
obj.find_type(s1,s2);

Вывод результата тестирования:
Exception AssertionError: Must be Admin
 Then the User must enter login Admin # features/steps/script_site_steps.py:17               


Проект включает в себя файлы:
script_site.py - основной скрипт
script_site_steps.py - файл c шагами по тестировке
sc_st.feature - файл сценария тестировки
script_site.exe - исполняемый файл со скриптом

Также требуется установка драйвера chromedriver.exe в текущие каталоги


