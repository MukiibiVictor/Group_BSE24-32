# Generated by Django 4.1.1 on 2022-09-28 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakestore', '0008_alter_cart_total_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_ordering',
        ),
    ]
