# Generated by Django 4.2.8 on 2024-02-01 08:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_addtocart'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('housename', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
            ],
        ),
    ]
