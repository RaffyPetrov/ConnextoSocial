from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, resolve_url, get_object_or_404
from django.views.generic import ListView
import clipboard
from ConnextoSocial.carvideos.models import CarVideo
from ConnextoSocial.common.forms import CommentForm, SearchForm, VideoCommentForm
from ConnextoSocial.common.models import Like, VideoLike
from ConnextoSocial.carphotos.models import CarPhoto


class HomePageView(ListView):
    model = CarPhoto
    template_name = 'templates/common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentForm()
        context['search_form'] = SearchForm(self.request.GET)

        user = self.request.user

        for photo in context['all_photos']:
            photo.has_liked = photo.like_set.filter(user=user).exists() if user.is_authenticated else False

        return context

    def get_queryset(self):
        # Fetch latest car photos, ordered by the date_of_publication field
        queryset = CarPhoto.objects.all().order_by('-date_of_publication')  # Most recent first

        car_name = self.request.GET.get('car_name')

        if car_name:
            queryset = queryset.filter(  # Filter the objects
                tagged_cars__car_name__icontains=car_name
            )
        return queryset  # return the new queryset


@login_required
def likes_functionality(request, photo_id: int = None, video_id: int = None):
    if photo_id:
        # Like for CarPhoto
        car_photo = get_object_or_404(CarPhoto, pk=photo_id)
        liked_object = Like.objects.filter(to_photo=car_photo, user=request.user).first()

        if liked_object:
            liked_object.delete()  # Remove the like
        else:
            Like.objects.create(to_photo=car_photo, user=request.user)  # Add the like

    elif video_id:
        # Like for CarVideo
        car_video = get_object_or_404(CarVideo, pk=video_id)
        liked_object = VideoLike.objects.filter(to_video=car_video, user=request.user).first()

        if liked_object:
            liked_object.delete()  # Remove the like
        else:
            VideoLike.objects.create(to_video=car_video, user=request.user)  # Add the like

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id or video_id}')


@login_required
def comment_on_car_photo(request, photo_id: int):
    """
    Handles commenting functionality for car photos.
    """
    if request.POST:
        photo = get_object_or_404(CarPhoto, pk=photo_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


@login_required
def comment_on_car_video(request, video_id: int):
    """
    Handles commenting functionality for car videos.
    """
    if request.POST:
        video = get_object_or_404(CarVideo, pk=video_id)
        comment_form = VideoCommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_video = video
            comment.user = request.user
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{video_id}')


def video_share_functionality(request, video_id: int):
    clipboard.copy(request.META.get('HTTP_HOST') + resolve_url('video-details', video_id))
    return redirect(request.META.get('HTTP_REFERER') + f'#{video_id}')


def photo_share_functionality(request, photo_id: int):
    clipboard.copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))
    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
