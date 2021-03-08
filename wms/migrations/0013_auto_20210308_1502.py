# Generated by Django 3.1.7 on 2021-03-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0012_auto_20210308_1457'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AlterField(
            model_name='atm',
            name='size',
            field=models.CharField(choices=[('EUR', 'Габарит EUR'), ('FIN', 'НЕГабарит FIN')], default='EUR', max_length=10),
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
