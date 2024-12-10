from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

from ConnextoSocial.cars.models import Cars
from ConnextoSocial.carphotos.validators import FileSizeValidator

UserModel = get_user_model()


class CarPhoto(models.Model):
    car_photo = models.ImageField(upload_to='car_photos/', validators=[FileSizeValidator(5)],)
    description = models.TextField(max_length=433, validators=[MinLengthValidator(10)], blank=True, null=True)
    location = models.CharField(max_length=66, blank=True, null=True)

    tagged_cars = models.ManyToManyField(to='cars.Cars', blank=True)

    date_of_publication = models.DateField(auto_now_add=True)

    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('photo-details', args=[str(self.id)])

    def __str__(self):
        return f"CarPhoto by {self.user} on {self.date_of_publication}"
