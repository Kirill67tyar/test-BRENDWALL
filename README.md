
# Тестовое задание BRENDWALL

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)



## __Установка на локальном компьютере__
1. Клонируйте репозиторий:
    ```
    git clone git@github.com:Kirill67tyar/test-BRENDWALL.git
    ```
    или
    ```
     git clone https://github.com/Kirill67tyar/test-BRENDWALL.git
    ```
2. Установите и активируйте виртуальное окружение:
    ```
    python3 -m venv venv
    source venv/Scripts/activate  - для Windows
    source venv/bin/activate - для Linux
    ```
3. Установите зависимости:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Выполните миграции:
    ```
    python manage.py migrate
    ```
5. Создайте суперпользователя:
    ```
    python manage.py createsuperuser
    ```
6. Запустите проект:
    ```
    python manage.py runserver
    ```
7. Сайт будет доступен на странице:
    ```
    http://127.0.0.1:8000/
    ```

### __Пример запросов/ответов__

##### Получение списка продуктов
#####Request: [GET] http://127.0.0.1:8000/api/products/ 
#####Response samples:
```
[
	{
		name: "p1",
		description: "описание p1",
		price: "5.10"
	},
	{
		name: "p2",
		description: "описание p2",
		price: "50.00"
	},
	{
		name: "p3",
		description: "описание p3",
		price: "3.00"
	}
```
#####Добавление нового продукта: Request: [POST] http://127.0.0.1:8000/api/products/ 
#####Response samples:
```
	{
		name: "new-pi",
		description: "описание new-pi",
		price: "3.14"
	}
```
##### Основная страница доступна [GET]/[POST] http://127.0.0.1:8000/


### __Технологии__
* [Python 3.10.12](https://www.python.org/doc/)
* [Django 4.2.10](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework  3.14.0](https://www.django-rest-framework.org/)

### Авторство

 1. [BrendWall](https://brendwall.ru/).
 2. [Кирилл Богомолов](https://github.com/Kirill67tyar).
