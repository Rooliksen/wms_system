# Generated by Django 3.1.7 on 2021-05-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0012_auto_20210505_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='status',
            field=models.CharField(choices=[('Принят', 'Принят'), ('Отгружен', 'Отгружен'), ('Резерв', 'Резерв')], default='Резерв', max_length=10),
        ),
    ]
