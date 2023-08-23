# Generated by Django 4.2.3 on 2023-08-23 18:36

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('flower_site', '0002_alter_bouquet_options_alter_component_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultationSignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU', verbose_name='Номер телефона')),
                ('is_active', models.BooleanField(default=True, verbose_name='Новый запрос на консультацию')),
            ],
            options={
                'verbose_name': 'Запись на консультацию флориста',
                'verbose_name_plural': 'Записи на консультацию флориста',
            },
        ),
        migrations.AddField(
            model_name='component',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Доступен для заказа'),
        ),
    ]
