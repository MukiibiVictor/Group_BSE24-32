# Generated by Django 4.1.1 on 2022-09-28 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakestore', '0004_cart_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
    ]
