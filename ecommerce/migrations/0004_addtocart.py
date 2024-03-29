# Generated by Django 4.2.8 on 2024-01-14 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_laptop_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddToCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.laptop')),
            ],
        ),
    ]
