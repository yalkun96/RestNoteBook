# Generated by Django 5.0.1 on 2024-01-28 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restbook', '0002_rest_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest',
            name='images',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
