# Generated by Django 5.1 on 2024-08-16 13:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='invalid phone number', regex='^(?:\\+98|0)?9\\d{9}$|^(?:\\+98|0)?(?:21|2[1-9]|3[1-9]|4[1-9])\\d{7,8}$')], verbose_name='Phone Number'),
        ),
    ]
