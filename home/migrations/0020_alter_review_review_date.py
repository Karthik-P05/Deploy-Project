# Generated by Django 5.0.6 on 2025-02-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_review_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
