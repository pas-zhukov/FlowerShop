# Flower Shop

Магазин цветов с оформлением заказов и доставкой по г. Москва.

# Установка зависимостей

Первым делом, скачайте код:
```shell
git clone https://github.com/pas-zhukov/FlowerShop.git
```

Создайте и активируйте виртуальное окружение:
```shell
virtualenv venv
source ./venv/bin/acticate
```

Установите зависимости:
```shell
pip install -r requirements.txt
```

# Запуск проекта

Примените миграции командой:
```shell
python3 manage.py migrate
```

Запустите dev-сервер:
```shell
python3 manage.py runserver
```

Перейдите по ссылке http://127.0.0.1:8000/ - на ней должна открыться главная страничка сайта.

# Доступ к админке и БД

Создайте аккаунт суперпользователя:
```shell
python3 manage.py createsuperuser
```

После запуска сервера перейдите по ссылке http://127.0.0.1:8000/admin/ и войдите через созданный аккаунт.