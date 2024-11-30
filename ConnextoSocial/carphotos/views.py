from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from ConnextoSocial.common.forms import CommentForm
from ConnextoSocial.carphotos.forms import CarPhotoAddForm, CarPhotoEditForm
from ConnextoSocial.carphotos.models import CarPhoto


class CarPhotoAddPage(LoginRequiredMixin, CreateView):
    model = CarPhoto
    template_name = 'templates/photos/car-photo-add-page.html'
    form_class = CarPhotoAddForm
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        form.save()
        return super().form_valid(form)


class CarPhotoEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CarPhoto
    form_class = CarPhotoEditForm
    template_name = 'templates/photos/car-photo-edit-page.html'

    def test_func(self):
        photo = get_object_or_404(CarPhoto, pk=self.kwargs['pk'])
        return self.request.user == photo.user

    def get_success_url(self):
        return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})


@login_required
def car_photo_delete(request, pk: int):
    photo = CarPhoto.objects.get(pk=pk)

    if request.user == photo.user:
        photo.delete()
    return redirect('home page')


class CarPhotoDetailsPage(LoginRequiredMixin, DetailView):
    model = CarPhoto
    template_name = 'templates/photos/car-photo-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['likes'] = self.object.like_set.all()
        context['comments'] = self.object.comment_set.all()
        context['comment_form'] = CommentForm()
        self.object.has_liked = self.object.like_set.filter(user=self.request.user).exists()

        return context
