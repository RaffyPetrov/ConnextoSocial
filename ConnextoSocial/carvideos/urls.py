from django.urls import path
from .views import CarVideosHomePageView, UploadVideoView, VideoDetailView, VideoEditView, video_delete

urlpatterns = [
    # Home page for CarVideos
    path('carvideos/homepage/', CarVideosHomePageView.as_view(), name='carvideos-homepage'),

    # Video upload page
    path('add/', UploadVideoView.as_view(), name='video-add'),

    # Video detail, edit, and delete
    path('<int:pk>/', VideoDetailView.as_view(), name='video-details'),
    path('<int:pk>/edit/', VideoEditView.as_view(), name='video-edit'),
    path('<int:pk>/delete/', video_delete, name='video-delete'),
]
