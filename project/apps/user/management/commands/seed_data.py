from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.product.models import Product

User = get_user_model()

class Command(BaseCommand):
    help = "Создаёт админа, пользователя и наполняет БД тестовыми данными"

    def handle(self, *args, **options):
        if not User.objects.filter(email = "admin@flight.ru").exists():
            User.objects.create_superuser(
                email = "admin@flight.ru",
                fio = "Admin",
                password = "QWEasd123",
            )
            self.stdout.write("Администратор admin@flight.ru создан")
        else:
            self.stdout.write("Администратор admin@flight.ru уже создан")

        if not User.objects.filter(email = "user@flight.ru").exists():
            User.objects.create_user(
                email = "user@flight.ru",
                fio = "User",
                password = "password",
            )
            self.stdout.write("Пользователь user@flight.ru создан")
        else:
            self.stdout.write("Пользователь user@flight.ru уже создан")

        if not Product.objects.exists():
            Product.objects.bulk_create([
                Product(
                    name="TOF-241, Томск-Москва",
                    description="Эконом-класс\nТомск - Время вылета: 12:00\nМосква - Время прилёта: 15:00",
                    price="15000"
                ),
                Product(
                    name="TOF-242, Томск-Казань",
                    description="Эконом-класс\nТомск - Время вылета: 13:00\nКазань - Время прилёта: 16:00",
                    price="8500"
                ),
                Product(
                    name="TOF-241, Томск-Иркутск",
                    description="Бизнес-класс\nТомск - Время вылета: 14:00\nИркутск - Время прилёта: 15:00",
                    price="20000"
                )
            ])
            self.stdout.write("БД Products наполнена тестовыми данными")
        else:
            self.stdout.write("БД Products уже наполнена тестовыми данными")
