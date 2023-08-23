from django.db import models


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




