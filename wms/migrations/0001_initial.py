# Generated by Django 3.1.7 on 2021-02-25 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateTimeField(verbose_name='Дата приема')),
                ('date_out', models.DateTimeField(verbose_name='Дата отгрузки')),
                ('name', models.CharField(max_length=200)),
                ('serial_num', models.CharField(max_length=200)),
                ('atm_id', models.CharField(max_length=200)),
                ('commentary', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('profile_pic', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OperationClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oper_name', models.CharField(max_length=200)),
                ('oper_cost', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.client')),
            ],
        ),
        migrations.CreateModel(
            name='OperationContractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oper_name', models.CharField(max_length=200)),
                ('oper_cost', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.contractor')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_name', models.CharField(max_length=200)),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.contractor')),
                ('operation_contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.operationcontractor')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.contractor')),
                ('rate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.rate')),
            ],
        ),
        migrations.CreateModel(
            name='OrderContractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage_order', models.CharField(max_length=200)),
                ('date_in', models.DateTimeField(verbose_name='Дата приема')),
                ('date_out', models.DateTimeField(verbose_name='Дата отгрузки')),
                ('driver', models.CharField(max_length=200)),
                ('driver_car', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('atm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.atm')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.client')),
                ('operation_contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.operationcontractor')),
                ('storage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.storage')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logistic_order', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('date_in', models.DateTimeField(verbose_name='Дата приема')),
                ('date_out', models.DateTimeField(verbose_name='Дата отгрузки')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('atm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.atm')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.client')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.customer')),
                ('operation_client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.operationclient')),
                ('storage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.storage')),
            ],
        ),
        migrations.AddField(
            model_name='atm',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.client'),
        ),
        migrations.AddField(
            model_name='atm',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.size'),
        ),
        migrations.AddField(
            model_name='atm',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.status'),
        ),
        migrations.AddField(
            model_name='atm',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms.storage'),
        ),
    ]
