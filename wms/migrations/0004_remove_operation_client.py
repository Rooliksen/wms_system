# Generated by Django 3.1.7 on 2021-03-16 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0003_auto_20210315_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='client',
        ),
    ]