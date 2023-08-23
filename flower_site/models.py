from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields.ranges import DateTimeRangeField
from django.utils import timezone
from datetime import timedelta


class ComponentType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип компонентов'
        verbose_name_plural = 'Типы компонентов'

    def __str__(self):
        return self.title


class Component(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    type = models.ForeignKey(ComponentType, on_delete=models.PROTECT, related_name='components', verbose_name='Тип компонента')

    is_available = models.BooleanField(default=True, verbose_name='Доступен для заказа')

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'

    def __str__(self):
        return self.title


class ComponentObject(models.Model):
    component = models.ForeignKey(Component, on_delete=models.PROTECT, related_name='object', verbose_name='Компонент')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    bouquet = models.ForeignKey('Bouquet', on_delete=models.PROTECT, related_name='component_objects', verbose_name='Для букета')

    class Meta:
        verbose_name = 'Компонент в заказе'
        verbose_name_plural = 'Компоненты в заказе'

    def __str__(self):
        return f'{self.component.title} - {self.quantity} шт.'


class BouquetCategory(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категория букетов'
        verbose_name_plural = 'Категории букетов'

    def __str__(self):
        return f'Категория: {self.title}'


class Bouquet(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='Фотография')
    height = models.IntegerField(verbose_name='Высота букета')
    width = models.IntegerField(verbose_name='Ширина букета')

    is_available = models.BooleanField(default=True, verbose_name='Доступен для заказа')

    categories = models.ManyToManyField(BouquetCategory, related_name='bouquets', verbose_name='Категории букета (теги)', blank=True)
    price = models.DecimalField(
        'Цена',
        decimal_places=2,
        max_digits=5,
        validators=[MinValueValidator(0)],
        null=True)  # FIXME УБРАТЬ НУЛЛ

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

    def __str__(self):
        return self.title


class OrderedBouquet(models.Model):
    bouquet = models.ForeignKey(Bouquet, on_delete=models.PROTECT, related_name='ordered', verbose_name='Букет')
    count = models.PositiveIntegerField('Количество')
    fixed_price = models.DecimalField(decimal_places=2,
                                      max_digits=5,
                                      validators=[MinValueValidator(0, 0)],
                                      verbose_name='Стоимость букета',
                                      null=True)  # FIXME УБРАТЬ НУЛЛ
    order = models.ForeignKey('Order', on_delete=models.PROTECT, related_name='bouquets')

    class Meta:
        verbose_name = 'Букет в заказе'
        verbose_name_plural = 'Букеты в заказах'

    def __str__(self):
        return f'{self.bouquet.title} - в заказе {self.order.id}'


class Order(models.Model):
    order_statuses = [(0, 'Необработанный'),
                      (1, 'В сборке'),
                      (2, 'В доставке'),
                      (3, 'Завершён')]

    @staticmethod
    def delivery_intervals():
        now = timezone.now().replace(minute=0, second=0, microsecond=0)
        tomorrow = now + timedelta(days=1)
        intervals = []
        for start_hour in range(10, 20, 2):
            tomorrow = tomorrow.replace(hour=start_hour)
            intervals.append(((tomorrow, tomorrow + timedelta(hours=2)),
                              f'Завтра ({tomorrow.strftime("%d.%m")}) с {start_hour} до {start_hour + 2}'))

        delivery_intervals = [
            ((timezone.now(), timedelta(hours=2)), 'Как можно скорее'),
            *intervals
        ]
        return delivery_intervals

    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = PhoneNumberField(region='RU', verbose_name='Номер телефона')
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(verbose_name='Адрес доставки')
    # TODO: починить интервал доставки
    # delivery_interval = DateTimeRangeField(verbose_name='Интервал доставки')  # TODO: сделать choices рабочими
    status = models.IntegerField(default=0, choices=order_statuses, db_index=True, verbose_name='Статус заказа')


class ConsultationSignUp(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = PhoneNumberField(region='RU', verbose_name='Номер телефона')

    is_active = models.BooleanField(default=True, verbose_name='Новый запрос на консультацию')

    class Meta:
        verbose_name = 'Запись на консультацию флориста'
        verbose_name_plural = 'Записи на консультацию флориста'

    def __str__(self):
        return f'Запрос на консультацию от {self.name}, номер: {self.phone}. {"Ожидает консультации." if self.is_active else "Консультация проводится или уже проведена."}'
