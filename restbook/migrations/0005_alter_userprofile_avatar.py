# Generated by Django 5.0.1 on 2024-01-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restbook', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='profile_images'),
        ),
    ]
