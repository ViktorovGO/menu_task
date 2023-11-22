# Web-приложение для построения древовидного меню.

## Установка и запуск

 Для MacOs и Linux вместо python использовать python3

## **1. Клонировать репозиторий:**
```
git clone https://github.com/ViktorovGO/menu_task.git
```

## **2. Перейти в папку проекта:**
```
cd menu_task/
```

## **3. Cоздать и активировать виртуальное окружение:**
```
python -m virtualenv venv
```

Для Windows:
```
venv\Scripts\activate.bat
```

Для MacOs/Linux:
```
source venv/bin/activate
```

## **4. Установить зависимости из файла requirements.txt:**
- Обновить пакетный менеджер pip
```
python -m pip install --upgrade pip
```

- Установить зависимости
```
pip install -r requirements.txt
```

## **5. Запустить веб сервер**
~~~
cd backend/
~~~
- Запустить сервер
~~~
python manage.py runserver
~~~

-Перейти по адресу 
~~~
http://localhost:8000/
~~~

