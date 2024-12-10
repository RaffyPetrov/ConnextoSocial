# Generated by Django 5.1.1 on 2024-12-09 10:25

import ConnextoSocial.carphotos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carphotos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carphoto',
            name='car_photo',
            field=models.ImageField(upload_to='profile_pictures/', validators=[ConnextoSocial.carphotos.validators.FileSizeValidator(5)]),
        ),
    ]
