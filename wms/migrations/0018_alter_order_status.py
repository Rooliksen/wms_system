# Generated by Django 3.2.2 on 2021-06-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0017_alter_orderitem_atm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Активна', 'Активна'), ('Закрыта', 'Закрыта'), ('Отменена', 'Отменена'), ('Черновик', 'Черновик')], default='Черновик', max_length=10),
        ),
    ]
