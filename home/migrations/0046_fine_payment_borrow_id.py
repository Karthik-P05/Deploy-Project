# Generated by Django 5.0.6 on 2025-04-22 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_remove_fine_payment_borrow_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fine_payment',
            name='borrow_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.borrowing_details'),
            preserve_default=False,
        ),
    ]
