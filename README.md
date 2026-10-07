# AviaProject — REST API для бронирования авиабилетов

Pet-проект: API сервиса бронирования и заказа авиабилетов.

## Стек

- Python 3.13
- Django + Django REST Framework
- PostgreSQL 15
- Docker + Docker Compose

## JWT

### Используется **HS256** — симметричный алгоритм,
оптимальный для монолитного приложения.

Альтернативы (RS256, ES256) применяются в микросервисах,
где public key нужен многим сервисам. Для проекта
с одним сервером это избыточно.

## Структура проекта

```
AviaProj/
├── deploy/
│   └── docker-compose.yml
├── project/
│   ├── apps/
│   │   ├── user/
│   │   ├── cart/
│   │   ├── orders/
│   │   └── product/
│   ├── config/
│   ├── Dockerfile
│   └── requirements.txt
└── collection/
    └── Api-Flight.postman_collection.json
```

## Запуск

### Требования

- Docker Desktop
- Git

### Шаги

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/Pf460/Projects_for_Department.git
   cd Projects_for_Department
   ```

2. Создать `.env`:

   ```bash
   cd project
   cp .env.example .env
   ```

3. Запустить контейнеры:

   ```bash
   cd ../deploy
   docker compose up --build -d
   ```

4. Заполнить БД тестовыми данными:

   ```bash
   docker compose exec web python manage.py seed_data
   ```

5. Открыть в браузере:

   - API: http://localhost:8000/api-flight/products
   - Админка: http://localhost:8000/admin/

## Учётные данные

| Роль | Email | Пароль |
|------|-------|--------|
| Администратор | `admin@flight.ru` | `QWEasd123` |
| Клиент | `user@flight.ru` | `password` |

## Эндпоинты

Базовый URL: `http://localhost:8000/api-flight`

Авторизация: заголовок `Authorization: Token <user_token>`

### Auth

| Метод | URL              | Описание                                                   |
|-------|------------------|------------------------------------------------------------|
| POST  | `/signup`        | Регистрация                                                |
| POST  | `/login`         | Вход                                                       |
| POST  | `/logout`        | Выход                                                      |
| GET   | `/profile`       | Профиль                                                    |
| PATCH | `/profile`       | Редактирование профиля                                     |
| POST  | `/token/refresh` | Получение нового accesse и refresh токена для пользователя |

### Products

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/products` | Список рейсов |

### Cart (только клиент)

| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/cart/{product_id}` | Добавить в корзину |
| GET | `/cart` | Просмотр корзины |
| DELETE | `/cart/{id}` | Удалить из корзины |

### Orders (только клиент)

| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/order` | Оформить заказ |
| GET | `/order` | История заказов |

### Admin (только администратор)

| Метод | URL | Описание |
|-------|-----|----------|
| POST | `/product` | Создать рейс |
| PATCH | `/product/{id}` | Редактировать рейс |
| DELETE | `/product/{id}` | Удалить рейс |

## Postman

Коллекция находится в `collection/Api-Flight.postman_collection.json`.
Импортируй её в Postman — все запросы уже настроены.
Переменная `{{host}}` = `http://localhost:8000/api-flight`.