# Generated by Django 3.2.9 on 2021-11-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0003_user_otp_validation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
