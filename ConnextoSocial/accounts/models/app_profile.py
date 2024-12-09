from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from ConnextoSocial.carphotos.validators import FileSizeValidator

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        validators=[FileSizeValidator(5)],
        default='profile_pictures/default.jpg',
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=433,
        validators=[MinLengthValidator(10)],
        blank=True, null=True
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name or self.first_name or self.last_name or "Anonymous"
