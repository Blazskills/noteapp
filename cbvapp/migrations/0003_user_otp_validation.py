# Generated by Django 3.2.9 on 2021-11-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0002_auto_20211123_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Otp_Validation',
            field=models.BooleanField(default=False),
        ),
    ]
