# Generated by Django 5.0.6 on 2025-02-20 10:34

import home.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_remove_borrowing_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='due_date',
            field=models.DateField(default=home.models.expiry),
        ),
    ]
