# Generated by Django 3.1.7 on 2021-04-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0008_auto_20210329_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='date_in',
            field=models.DateField(null=True, verbose_name='Дата приема'),
        ),
        migrations.AlterField(
            model_name='atm',
            name='date_out',
            field=models.DateField(null=True, verbose_name='Дата отгрузки'),
        ),
    ]