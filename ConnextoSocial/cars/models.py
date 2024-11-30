from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()


class Cars(models.Model):
    car_name = models.CharField(max_length=70)
    car_model = models.CharField(max_length=40)

    car_photo = models.URLField()

    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.car_name}-{self.id}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.car_name
