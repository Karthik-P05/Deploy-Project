# Generated by Django 5.0.6 on 2025-02-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_borrowing_approved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Returned', 'Returned')], default='Pending', max_length=20),
        ),
    ]
