# Generated by Django 3.2.2 on 2021-05-30 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0014_rename_orderphoto_atmphoto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atmphoto',
            old_name='photo',
            new_name='image',
        ),
    ]
