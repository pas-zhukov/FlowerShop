from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ComponentType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип компонентов'
        verbose_name_plural = 'Типы компонентов'

    def __str__(self):
        return self.title


class Component(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    type = models.ForeignKey(ComponentType, on_delete=models.PROTECT)

    is_available = models.BooleanField(default=True, verbose_name='Доступен для заказа')

    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'

    def __str__(self):
        return self.title


class ComponentObject(models.Model):
    component = models.ForeignKey(Component, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    bouquet = models.ForeignKey('Bouquet', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Компонент в заказе'
        verbose_name_plural = 'Компоненты в заказе'

    def __str__(self):
        return f'{self.component.title} - {self.quantity} шт.'


class Bouquet(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(verbose_name='Фотография')
    height = models.IntegerField(verbose_name='Высота букета')
    width = models.IntegerField(verbose_name='Ширина букета')

    is_available = models.BooleanField(default=True, verbose_name='Доступен для заказа')

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'

    def __str__(self):
        return self.title


class ConsultationSignUp(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = PhoneNumberField(region='RU', verbose_name='Номер телефона')
    is_active = models.BooleanField(default=True, verbose_name='Новый запрос на консультацию')

    class Meta:
        verbose_name = 'Запись на консультацию флориста'
        verbose_name_plural = 'Записи на консультацию флориста'

    def __str__(self):
        return f'Запрос на консультацию от {self.name}, номер: {self.phone}. {"Ожидает консультации." if self.is_active else "Консультация проводится или уже проведена."}'

