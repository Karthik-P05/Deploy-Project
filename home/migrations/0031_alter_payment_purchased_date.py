# Generated by Django 5.0.6 on 2025-03-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_payment_purchased_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='purchased_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
