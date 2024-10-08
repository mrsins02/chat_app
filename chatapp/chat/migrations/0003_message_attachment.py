# Generated by Django 5.1 on 2024-08-18 16:45

import chatapp.utils.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=chatapp.utils.models.upload_location, verbose_name='Attachment'),
        ),
    ]
