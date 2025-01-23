# Generated by Django 5.1.4 on 2025-01-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eisaalShop', '0012_orders_rename_shopproducts_addshopproducts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='total_price',
            new_name='order_amount',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='razorpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='razorpay_signature',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='status',
        ),
        migrations.AddField(
            model_name='orders',
            name='razorpay_key_id',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='orders',
            name='razorpay_order_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
