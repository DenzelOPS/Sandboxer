# Generated by Django 4.0.4 on 2024-02-14 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_telegram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
