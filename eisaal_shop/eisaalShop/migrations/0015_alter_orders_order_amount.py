# Generated by Django 5.1.4 on 2025-01-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eisaalShop', '0014_rename_razorpay_key_id_orders_razorpay_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_amount',
            field=models.CharField(default=0, max_length=100000, null=True),
        ),
    ]
