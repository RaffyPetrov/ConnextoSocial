# Generated by Django 5.1.1 on 2024-12-09 10:31

import ConnextoSocial.carphotos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carphotos', '0002_alter_carphoto_car_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carphoto',
            name='car_photo',
            field=models.ImageField(upload_to='car_photos/', validators=[ConnextoSocial.carphotos.validators.FileSizeValidator(5)]),
        ),
    ]
