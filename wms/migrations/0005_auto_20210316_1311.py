# Generated by Django 3.1.7 on 2021-03-16 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0004_remove_operation_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='operation',
        ),
        migrations.DeleteModel(
            name='Operation',
        ),
    ]