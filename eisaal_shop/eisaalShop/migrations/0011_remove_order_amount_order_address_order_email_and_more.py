# Generated by Django 5.1.4 on 2025-01-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eisaalShop', '0010_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=0, max_length=12),
        ),
        migrations.AddField(
            model_name='order',
            name='qut',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.CharField(default=0, max_length=100000),
        ),
    ]
