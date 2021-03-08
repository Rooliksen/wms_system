# Generated by Django 3.1.7 on 2021-03-07 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0005_auto_20210307_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='rate',
            new_name='rate_in',
        ),
        migrations.AddField(
            model_name='storage',
            name='rate_out',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='storage',
            name='rate_pallet',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='storage',
            name='rate_volume',
            field=models.IntegerField(null=True),
        ),
    ]
