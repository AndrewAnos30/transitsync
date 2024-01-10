# Generated by Django 4.2.7 on 2024-01-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashierTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionID', models.CharField(blank=True, max_length=20, null=True)),
                ('CashierSN', models.CharField(blank=True, max_length=100, null=True)),
                ('CommuterSN', models.CharField(blank=True, max_length=100, null=True)),
                ('CashIn', models.FloatField(blank=True, default=0, null=True)),
                ('paidAmount', models.FloatField(blank=True, default=0, null=True)),
                ('change', models.FloatField(blank=True, default=0, null=True)),
                ('DateIn', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CurrentDate', models.DateField(blank=True, null=True)),
                ('CurrentFarePUJ', models.FloatField(blank=True, default=0, null=True)),
                ('CurrentSucceedingPUJ', models.FloatField(blank=True, default=0, null=True)),
                ('CurrentDiesel', models.FloatField(blank=True, default=0, null=True)),
                ('CurrentSucceedingBus', models.FloatField(blank=True, default=0, null=True)),
                ('CurrentFareBus', models.FloatField(blank=True, default=0, null=True)),
                ('Num', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataCrawl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CrawlDate', models.CharField(blank=True, default=0, max_length=200, null=True)),
                ('CrawlPHP', models.FloatField(blank=True, default=0, null=True)),
                ('CrawlUSD', models.FloatField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransportationRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitudeIN', models.FloatField(blank=True, null=True)),
                ('latitudeIN', models.FloatField(blank=True, null=True)),
                ('longitudeOUT', models.FloatField(blank=True, null=True)),
                ('latitudeOUT', models.FloatField(blank=True, null=True)),
                ('scan_type', models.CharField(blank=True, max_length=20, null=True)),
                ('extracted_data', models.TextField(blank=True, null=True)),
                ('scan_date', models.DateTimeField(auto_now_add=True)),
                ('TranspoSN', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('user', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('km', models.FloatField(blank=True, null=True)),
                ('commuterStatus', models.CharField(blank=True, max_length=25, null=True)),
                ('TranspoType', models.CharField(blank=True, max_length=25, null=True)),
                ('processed', models.BooleanField(default=False)),
                ('penalty', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TranspoType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
