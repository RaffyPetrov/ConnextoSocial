from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from ConnextoSocial.cars.forms import CarAddForm
from .models import CarVideo
from .forms import CarVideoAddForm, CarVideoEditForm
from django.shortcuts import redirect, get_object_or_404
from ..common.forms import VideoCommentForm, CarVideoSearchForm


class CarVideosHomePageView(ListView):
    model = CarVideo
    template_name = 'templates/carvideos/carvideo-home-page.html'
    context_object_name = 'all_videos'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = VideoCommentForm()
        context['search_form'] = CarVideoSearchForm(self.request.GET)

        user = self.request.user

        # If the request is for a specific user's profile, get their videos
        if 'user_pk' in self.kwargs:
            context['all_videos'] = CarVideo.objects.filter(user__pk=self.kwargs['user_pk']).order_by('-uploaded_at')

        # Check if the current user has liked the videos
        for video in context['all_videos']:
            video.has_liked = video.videolike_set.filter(user=user).exists() if user.is_authenticated else False

        return context

    def get_queryset(self):
        # Fetch all car videos ordered by the most recent `uploaded_at`
        queryset = CarVideo.objects.all().order_by('-uploaded_at')

        # Get the search parameter from the request
        car_name = self.request.GET.get('car_name')

        if car_name:
            queryset = queryset.filter(  # Filter the objects
                tagged_cars__car_name__icontains=car_name
            )
        return queryset  # return the new queryset


class UploadVideoView(LoginRequiredMixin, CreateView):
    model = CarVideo
    form_class = CarVideoAddForm
    template_name = 'templates/carvideos/upload_video.html'
    success_url = reverse_lazy('carvideos-homepage')  # Redirect to the video list after upload

    def form_valid(self, form):
        # Save the video and associate it with the current user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include the car form if necessary, similar to CarAddForm in the car photos example
        if 'car_form' not in context:
            context['car_form'] = CarAddForm()
        return context

    def form_valid(self, form):
        vide_form = CarVideoAddForm(self.request.POST or None)
        video_instance = None

        if vide_form.is_valid():
            video_instance = vide_form.save(commit=False)
            video_instance.user = self.request.user
            video_instance.save()

        # Save the video and associate it with the car(s)
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        # If a car was created, add it to tagged_cars
        if video_instance:
            self.object.tagged_cars.add(video_instance)

        self.object.save()
        return super().form_valid(form)


# View to edit an existing video
class VideoEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CarVideo
    form_class = CarVideoEditForm
    template_name = 'templates/carvideos/video_edit_page.html'

    def test_func(self):
        video = get_object_or_404(CarVideo, pk=self.kwargs['pk'])
        return self.request.user == video.user  # Only allow the user who uploaded the video to edit it

    def get_success_url(self):
        return reverse_lazy('video-details', kwargs={'pk': self.object.pk})


# Function to delete a video
@login_required
def video_delete(request, pk: int):
    video = get_object_or_404(CarVideo, pk=pk)
    if request.user == video.user:
        video.delete()
    return redirect('video_list')  # Redirect to video list after deletion


# View to display details of a specific video
class VideoDetailView(LoginRequiredMixin, DetailView):
    model = CarVideo
    template_name = 'templates/carvideos/video_details.html'  # Corrected template path
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = self.object  # Get the current video object

        if self.object:
            context['video'] = self.object
            context['likes'] = video.videolike_set.all()  # Get all likes for this video
            context['comments'] = video.videocomment_set.all()  # Get all comments for this video
            context['video_comment_form'] = CarVideoSearchForm()  # Assuming this is your comment form

            # Check if the user has liked this video
            context['has_liked'] = video.videolike_set.filter(user=self.request.user).exists()
        else:
            context['video'] = None

        return context
