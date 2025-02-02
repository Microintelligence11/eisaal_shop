# Generated by Django 5.1.4 on 2025-01-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eisaalShop', '0009_alter_shopproducts_sno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=300, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=300, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(default='Pending', max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
