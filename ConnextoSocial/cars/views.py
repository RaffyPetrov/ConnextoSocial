from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from ConnextoSocial.common.forms import CommentForm
from ConnextoSocial.cars.forms import CarAddForm, CarEditForm, CarDeleteForm
from ConnextoSocial.cars.models import Cars


class CarAddPage(LoginRequiredMixin, CreateView):
    model = Cars
    form_class = CarAddForm
    template_name = 'templates/photos/car-photo-add-page.html'

    def form_valid(self, form):
        car = form.save(commit=False)
        car.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('photo-add')


class CarEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cars
    template_name = 'templates/cars/car-edit-page.html'
    form_class = CarEditForm
    slug_url_kwarg = 'car_slug'

    def test_func(self):
        car = get_object_or_404(Cars, slug=self.kwargs['car_slug'])
        return self.request.user == car.user

    def get_success_url(self):
        return reverse_lazy(
            'car-details',
            kwargs={
                'username': self.kwargs['username'],
                'car_slug': self.kwargs['car_slug'],
            }
        )


class CarDeletePage(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cars
    template_name = 'templates/cars/car-delete-page.html'
    slug_url_kwarg = 'car_slug'
    form_class = CarDeleteForm

    def get_success_url(self):
        return reverse_lazy(
            'profile-details',
            kwargs={
                'pk': self.request.user.pk,
            }
        )

    def test_func(self):
        car = get_object_or_404(Cars, slug=self.kwargs['car_slug'])
        return self.request.user == car.user

    def get_initial(self) -> dict:
        return self.get_object().__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'data': self.get_initial(),
        })

        return kwargs


class CarDetailsPage(LoginRequiredMixin, DetailView):
    model = Cars
    template_name = 'templates/cars/car-details-page.html'
    slug_url_kwarg = 'car_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['all_photos'] = context['car'].photo_set.all()

        context['comment_form'] = CommentForm()

        all_photos = context['car'].photo_set.all()

        for photo in all_photos:
            photo.has_liked = photo.like_set.filter(user=self.request.user).exists()

        context['all_photos'] = all_photos

        return context
