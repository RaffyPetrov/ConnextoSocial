from ConnextoSocial.carphotos.models import CarPhoto
from ConnextoSocial.carvideos.models import CarVideo  # Import CarVideo model
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Comment model for CarPhotos
class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']

    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(to=CarPhoto, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.to_photo}"


# Like model for CarPhotos
class Like(models.Model):
    to_photo = models.ForeignKey(to=CarPhoto, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('to_photo', 'user')  # Prevent duplicate likes

    def __str__(self):
        return f"Like by {self.user} on {self.to_photo}"


# Comment model for CarVideos
class VideoComment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']

    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_video = models.ForeignKey(to=CarVideo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.to_video}"


# Like model for CarVideos
class VideoLike(models.Model):
    to_video = models.ForeignKey(to=CarVideo, on_delete=models.CASCADE)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('to_video', 'user')  # Prevent duplicate likes

    def __str__(self):
        return f"Like by {self.user} on {self.to_video}"
