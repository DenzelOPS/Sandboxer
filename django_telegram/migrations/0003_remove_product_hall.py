# Generated by Django 4.0.4 on 2024-02-14 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_telegram', '0002_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='hall',
        ),
    ]
