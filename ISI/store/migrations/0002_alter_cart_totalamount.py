# Generated by Django 5.0.3 on 2024-03-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='totalAmount',
            field=models.FloatField(default=0),
        ),
    ]
