# Generated by Django 4.2.8 on 2024-03-01 11:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_remove_addtocart_razor_pay_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$')]),
        ),
    ]
