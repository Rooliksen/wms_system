# Generated by Django 3.2.2 on 2021-06-01 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0016_atmphoto_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='atm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wms.atm'),
        ),
    ]