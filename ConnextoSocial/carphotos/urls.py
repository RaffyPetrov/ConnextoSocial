from django.urls import path, include
from ConnextoSocial.carphotos import views

urlpatterns = [
    path('add/', views.CarPhotoAddPage.as_view(), name='photo-add'),
    path('<int:pk>/', include([
        path('', views.CarPhotoDetailsPage.as_view(), name='photo-details'),
        path('edit/', views.CarPhotoEditPage.as_view(), name='photo-edit'),
        path('delete/', views.car_photo_delete, name='photo-delete'),
    ])),
]