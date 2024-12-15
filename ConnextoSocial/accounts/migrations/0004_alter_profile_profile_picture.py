# Generated by Django 5.1.1 on 2024-12-15 15:31

import ConnextoSocial.carphotos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/person.png', null=True, upload_to='profile_pictures/', validators=[ConnextoSocial.carphotos.validators.FileSizeValidator(5)]),
        ),
    ]
