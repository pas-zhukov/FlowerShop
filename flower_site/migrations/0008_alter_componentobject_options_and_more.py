# Generated by Django 4.2.3 on 2023-08-26 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_site', '0007_remove_order_delivery_interval'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentobject',
            options={'verbose_name': 'Компонент в букете', 'verbose_name_plural': 'Компоненты в букете'},
        ),
        migrations.AlterModelOptions(
            name='orderedbouquet',
            options={'verbose_name': 'Букет в заказе', 'verbose_name_plural': 'Букеты в заказе'},
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_interval',
            field=models.CharField(default='Как можно скорее', max_length=20, verbose_name='Интервал доставки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(choices=[(0, 'Не оплачен'), (1, 'Оплачен')], default=0, verbose_name='Статус оплаты'),
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='orderedbouquet',
            name='count',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='orderedbouquet',
            name='fixed_price',
            field=models.DecimalField(decimal_places=5, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(0, 0)], verbose_name='Стоимость букета'),
        ),
    ]