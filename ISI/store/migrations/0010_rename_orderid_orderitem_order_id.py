# Generated by Django 5.0.3 on 2024-03-09 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_order_orderamount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='orderID',
            new_name='order_ID',
        ),
    ]