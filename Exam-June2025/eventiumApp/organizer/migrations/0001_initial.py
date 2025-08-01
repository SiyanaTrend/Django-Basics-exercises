# Generated by Django 5.2.3 on 2025-06-22 08:01

import django.core.validators
import organizer.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(help_text='*Allowed names contain letters, digits, spaces, and hyphens.', max_length=110, unique=True, validators=[organizer.validators.CompanyNameValidator(), django.core.validators.MinLengthValidator(2)])),
                ('phone_number', models.CharField(error_messages={'unique': 'That phone number is already in use!'}, max_length=15, unique=True, validators=[organizer.validators.PhoneNumberValidator()])),
                ('secret_key', models.CharField(help_text='*Pick a combination of 4 unique digits.', max_length=4, validators=[organizer.validators.SecretKeyValidator()])),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
