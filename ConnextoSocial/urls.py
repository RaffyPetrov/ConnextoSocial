from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ConnextoSocial.common.urls')),
    path('accounts/', include('ConnextoSocial.accounts.urls')),
    path('cars/', include('ConnextoSocial.cars.urls')),
    path('photos/', include('ConnextoSocial.carphotos.urls')),
    path('carvideos/', include('ConnextoSocial.carvideos.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
