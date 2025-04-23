**Как запустить pytest в режиме Debug**
---
+ Создаем файл конфигурации запуска (launch.json) в папке с проектом.  
+ Открываем VSCode и переходим в окно отладки (Debug).  
+ Нажмаем на шестерёнку рядом с надписью «Run and Debug», чтобы создать новый файл конфигурации запуска.
~~~
launch.json
~~~  
Вставляем в файл и запускаем Run and Debug (Ctrl + Shift + D) + Start Debugging (F5)
~~~
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Test",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "-k",                 // Включаем режим фильтрации тестов
                "test_scenarios",   // Имя теста (без полного пути к файлу)
                "${workspaceFolder}"  // Рабочая директория (корневая папка проекта) -> workspaceFolder Оставляем без изменений
            ],
            "justMyCode": false
        }
    ]
}
~~~
---
"name" — имя конфигурации, которое появится в списке запускаемых профилей.  
"type" — тип среды выполнения («python»).  
"request" — режим отладчика ("launch").  
"module" — модуль Python, который должен выполняться («pytest»).  
"args" — аргументы команды Pytest (например, опции "--pdb" позволяют интерактивное выполнение теста с возможностью останова при ошибке).  
"justMyCode" — настройка, позволяющая включить/отключить игнорирование стороннего кода (False означает включение возможности ставить точки останова во всех модулях, включая внешние библиотеки).  


---
**Если необходимо запустить конкретный тест на выбор, то через двоеточие вставляем имя класса и метода теста.**
В активированнои виртуальном окружении вводим команду в терминал и получаем список доступных тестов.  
~~~
pytest --collect-only
~~~
~~~
<Dir de-project-bibip>
  <Package tests>
    <Module test_scenarios.py>
      <Class TestCarServiceScenarios>
        <Function test_add_new_car>
        <Function test_sell_car>
        <Function test_list_cars_by_available_status>
        <Function test_list_full_info_by_vin>
        <Function test_update_vin>
        <Function test_delete_sale>
        <Function test_top_3_models_by_sales>
~~~
Вставляем нужный тест в "args" и Запускаем Run and Debug (Ctrl + Shift + D) + Start Debugging (F5)
~~~
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Test",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": [
                "-k",                 // Включаем режим фильтрации тестов
                "test_add_new_car",   // Имя теста (без полного пути к файлу)
                "${workspaceFolder}"  // Рабочая директория (корневая папка проекта) -> workspaceFolder Оставляем без изменений
            ],
            "justMyCode": false
        }
    ]
}
~~~
