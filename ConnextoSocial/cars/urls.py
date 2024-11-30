from django.urls import path, include

from ConnextoSocial.cars import views

urlpatterns = [
    path('add/', views.CarAddPage.as_view(), name='add-car'),
    path('<str:username>/car/<slug:car_slug>/', include([
        path('', views.CarDetailsPage.as_view(), name='car-details'),
        path('edit/', views.CarEditPage.as_view(), name='edit-car'),
        path('delete/', views.CarDeletePage.as_view(), name='delete-car'),
    ]))
]
