# Generated by Django 4.2.8 on 2024-02-06 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_addtocart_razor_pay_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocart',
            name='laptop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.laptop'),
        ),
    ]
