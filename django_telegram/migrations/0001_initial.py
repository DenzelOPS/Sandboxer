# Generated by Django 4.0.4 on 2024-02-14 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile_phone', models.CharField(max_length=200)),
                ('large_families', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_name', models.CharField(max_length=200)),
                ('discount_percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit', models.CharField(choices=[('безлимит', 'безлимит'), ('1 час', '1 час'), ('30 минут', '30 минут')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_hall', to='django_telegram.hall')),
            ],
        ),
        migrations.CreateModel(
            name='ClientOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_product', to='django_telegram.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_product', to='django_telegram.product')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='payment_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_payment', to='django_telegram.payment'),
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1)),
                ('status', models.BooleanField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_child', to='django_telegram.client')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_discount', to='django_telegram.discount')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_hall', to='django_telegram.hall')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_partner', to='django_telegram.partner')),
                ('visit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_visit', to='django_telegram.visit')),
            ],
        ),
    ]
