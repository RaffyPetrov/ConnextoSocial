from django.contrib import admin
from ConnextoSocial.carphotos.models import CarPhoto


# Register your models here.
@admin.register(CarPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_cars')

    @staticmethod
    def get_tagged_cars(obj):
        return ', '.join(str(cars) for cars in obj.tagged_cars.all())
