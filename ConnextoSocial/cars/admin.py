from django.contrib import admin

from ConnextoSocial.cars.models import Cars


@admin.register(Cars)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'slug')
