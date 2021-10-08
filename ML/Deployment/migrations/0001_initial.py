# Generated by Django 3.2.8 on 2021-10-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deployed_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.IntegerField(default=0, max_length=100)),
                ('House_Type', models.CharField(choices=[('h', 'house,cottage,villa, semi,terrace'), ('u', 'duplex'), ('t', 'townhouse')], default='select housetype', max_length=100)),
                ('number_of_bedrooms', models.IntegerField(default=0, max_length=100)),
                ('bathrooms', models.IntegerField(default=0, max_length=100)),
                ('number_of_car_spots', models.IntegerField(default=0, max_length=100)),
                ('landsize', models.FloatField(default=0.0)),
                ('building_area', models.FloatField(default=0.0)),
            ],
        ),
    ]