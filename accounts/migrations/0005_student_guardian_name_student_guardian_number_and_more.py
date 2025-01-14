# Generated by Django 5.0.4 on 2024-12-16 05:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_feeshistory_fee_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='guardian_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be between 9 and 15 digits.', regex='^\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_relation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
