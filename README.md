# Watcher of Friends Online

Программа ввыводит список друзей пользователя в соц. сети ["Вконтакте"](vk.com), которые имеют статус "Online". Программа использует вызовы методов [API ВКонтакте](https://vk.com/dev/manuals)

# Установка

Для запуска программы требуется установленный Python 3.  
Используте команду pip для установки сторонних библиотек из файла зависимостей (или pip3 если есть конфликт с предустановленным Python 2):
```bash
pip install -r requirements.txt # В качестве альтернативы используйте pip3
```
Рекомендуется устанавливать зависимости в виртуальном окружении, используя [virtualenv](https://github.com/pypa/virtualenv), [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) или [venv](https://docs.python.org/3/library/venv.html).

# Использование

Пример запуска в Linux, Python 3.5.2:

```bash
$ python vk_friends_online.py
```
После запуска программы пользователю необходимо ввести логин и пароль от соц. сети "Вконтакте".
Пример вывода результатов:
```bash
User login: +7xxxxxxxxxx
Password:
Online friends: 3
John Doe
John Smith
Judy Doe
```

# Цели проекта

Код написан для образовательных целей. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
