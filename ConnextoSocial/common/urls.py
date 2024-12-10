from django.urls import path
from ConnextoSocial.common.views import HomePageView, comment_on_car_photo, comment_on_car_video, \
    photo_share_functionality, video_share_functionality, likes_functionality

urlpatterns = (
    # Home page
    path('', HomePageView.as_view(), name='home page'),

    path('like/photo/<int:photo_id>/', likes_functionality, name='like'),
    path('like/video/<int:video_id>/', likes_functionality, name='carvideos-like'),

    path('share/photo/<int:photo_id>/', photo_share_functionality, name='photo-share'),
    # Share functionality for CarPhotos
    path('share/video/<int:video_id>/', video_share_functionality, name='video-share'),


    path('comment/photo/<int:photo_id>/', comment_on_car_photo, name='comment_on_car_photo'),
    path('comment/video/<int:video_id>/', comment_on_car_video, name='comment_on_car_video'),

)
