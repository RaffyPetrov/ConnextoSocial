from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ConnextoSocial.common.urls')),
    path('accounts/', include('ConnextoSocial.accounts.urls')),
    path('cars/', include('ConnextoSocial.cars.urls')),
    path('photos/', include('ConnextoSocial.photos.urls')),

]