# Generated by Django 3.1.7 on 2021-03-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0004_auto_20210307_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='rate',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
    ]