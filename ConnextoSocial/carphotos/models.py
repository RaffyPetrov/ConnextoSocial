from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from ConnextoSocial.cars.models import Cars
from ConnextoSocial.carphotos.validators import FileSizeValidator

UserModel = get_user_model()


class CarPhoto(models.Model):
    car_photo = models.ImageField(validators=[FileSizeValidator(5)],)
    description = models.TextField(max_length=433, validators=[MinLengthValidator(10)], blank=True, null=True)
    location = models.CharField(max_length=66, blank=True, null=True)

    tagged_cars = models.ManyToManyField('cars.Cars', blank=True)

    date_of_publication = models.DateField(auto_now_add=True)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)