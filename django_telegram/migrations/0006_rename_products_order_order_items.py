# Generated by Django 4.0.4 on 2024-02-14 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_telegram', '0005_rename_clientorder_orderitem_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='order_items',
        ),
    ]
