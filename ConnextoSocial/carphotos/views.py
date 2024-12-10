from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from ConnextoSocial.cars.forms import CarAddForm
from ConnextoSocial.common.forms import CommentForm
from ConnextoSocial.carphotos.forms import CarPhotoAddForm, CarPhotoEditForm
from ConnextoSocial.carphotos.models import CarPhoto


class CarPhotoAddPage(LoginRequiredMixin, CreateView):
    model = CarPhoto
    template_name = 'templates/photos/car-photo-add-page.html'
    form_class = CarPhotoAddForm
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include the car form in the context
        if 'car_form' not in context:
            context['car_form'] = CarAddForm()
        return context

    def form_valid(self, form):
        car_form = CarAddForm(self.request.POST or None)
        car_instance = None
        if car_form.is_valid():
            car_instance = car_form.save(commit=False)
            car_instance.user = self.request.user
            car_instance.save()

        # Save the photo and associate it with the car(s)
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        # If a car was created, add it to tagged_cars
        if car_instance:
            self.object.tagged_cars.add(car_instance)

        self.object.save()

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

        if self.object:
            context['photo'] = self.object
            context['likes'] = self.object.like_set.all()
            context['comments'] = self.object.comment_set.all()
            context['comment_form'] = CommentForm()

            # Check if the user has liked this photo
            context['photo'].has_liked = self.object.like_set.filter(user=self.request.user).exists()
        else:
            context['photo'] = None

        return context
