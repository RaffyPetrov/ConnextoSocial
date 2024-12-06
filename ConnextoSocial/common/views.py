from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, resolve_url
from django.views.generic import ListView
from pyperclip import copy
from ConnextoSocial.common.forms import CommentForm, SearchForm
from ConnextoSocial.common.models import Like
from ConnextoSocial.carphotos.models import CarPhoto


class HomePageView(ListView):
    model = CarPhoto
    template_name = 'templates/common/home-page.html'
    context_object_name = 'all_photos'
    paginate_by = 5

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
def likes_functionality(request, photo_id: int):
    liked_object = Like.objects.filter(
        to_photo_id=photo_id,
        user=request.user
    ).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo_id=photo_id, user=request.user)
        like.save()

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


def share_functionality(request, photo_id: int):
    copy(request.META.get('HTTP_HOST') + resolve_url('photo-details', photo_id))

    return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')


@login_required
def comment_functionality(request, photo_id: int):
    if request.POST:
        photo = CarPhoto.objects.get(pk=photo_id)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META.get('HTTP_REFERER') + f'#{photo_id}')
