# Generated by Django 3.1.7 on 2021-03-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0009_storage_rate_oversize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='rate_oversize',
            new_name='rate_oversize_in',
        ),
        migrations.AddField(
            model_name='storage',
            name='rate_oversize_out',
            field=models.DecimalField(decimal_places=2, max_digits=9999, null=True),
        ),
        migrations.AddField(
            model_name='storage',
            name='rate_oversize_pallet',
            field=models.DecimalField(decimal_places=2, max_digits=9999, null=True),
        ),
    ]
