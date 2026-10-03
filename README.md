#AviaProject
REST API сервиса бронирования авиабилетов для компании "Просто летать"
(По совместительству тестовое задание на напраление Backend IT-кафедры ТТИТ)

#Стек

-python 3.13

-Django 6.1.1

-DRF 6.1.1

-PostgreSQL 15

-Docker + Docker compose

#Структура проекта

-AviaProj/

--.venv/

--collection/

---Api-Flight.postman_collection.json

--deploy/

---docker-compose.yml

--project/

---apps/

----user/

----cart/

----orders/

----product/

---config/

---media/

----avatars/

-----default.jpg

---.env.example

---Dockerfile

---requirements.txt

#Запуск

###Требования

-Docker Desktop

-Git

-Postman Desktop (для проверки)

###Шаги

1.Клонировать репозиторий
```bash
git clone https://github.com/Pf460/Projects_for_Department.git
cd Projects_for_Department
```

2.Создать .env из шаблона
```bash
cd project
cp .env.example .env
```

3. Запусти контейнеры
```bash
cd ../deploy
docker compose up --build -d
```

4. Заполни БД seed-данными
```bash
docker compose exec web python manage.py seed_data
```

#Учётные данные

###admin

-email: admin@flight.ru

-password: QWEasd123

###user

-email: user@flight.ru

-password: password

5. Открой в браузере:

-API: http://localhost:8000/api-flight/

-Админка: http://localhost:8000/admin/
