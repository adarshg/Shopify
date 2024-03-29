# Generated by Django 4.2.8 on 2024-02-09 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0011_alter_addtocart_laptop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtocart',
            name='razor_pay_order_id',
        ),
        migrations.RemoveField(
            model_name='addtocart',
            name='razor_pay_payment_id',
        ),
        migrations.RemoveField(
            model_name='addtocart',
            name='razor_pay_payment_signature',
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('razorpay_order_id', models.CharField(max_length=100)),
                ('razorpay_payment_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
