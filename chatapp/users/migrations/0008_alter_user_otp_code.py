# Generated by Django 5.1 on 2024-08-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_options_alter_user_otp_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp_code',
            field=models.CharField(blank=True, default='12345', max_length=5, verbose_name='OTP Code'),
        ),
    ]
