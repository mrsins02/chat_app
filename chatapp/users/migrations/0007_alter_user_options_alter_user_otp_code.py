# Generated by Django 5.1 on 2024-08-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_code',
            field=models.CharField(blank=True, default='12345', max_length=4, verbose_name='OTP Code'),
        ),
    ]
