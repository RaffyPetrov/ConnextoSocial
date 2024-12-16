from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
from django.urls import reverse
from .validators import validate_video_length  # Import your custom validator

UserModel = get_user_model()


class CarVideo(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.FileField(
        upload_to='car_videos/',
        validators=[validate_video_length]
    )
    description = models.TextField(
        max_length=433,
        validators=[MinLengthValidator(10)],
        blank=True,
        null=True
    )
    tagged_cars = models.ManyToManyField(to='cars.Cars', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('video-details', args=[str(self.id)])

    def __str__(self):
        return self.title
