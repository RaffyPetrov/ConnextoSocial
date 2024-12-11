from django import forms
from .models import CarVideo


class CarVideoBaseForm(forms.ModelForm):
    class Meta:
        model = CarVideo
        exclude = ('user',)  # Exclude the user field to be set automatically


class CarVideoAddForm(forms.ModelForm):
    class Meta:
        model = CarVideo
        fields = ['title', 'description', 'video', 'tagged_cars']


class CarVideoEditForm(CarVideoBaseForm):
    class Meta(CarVideoBaseForm.Meta):
        exclude = ('user', 'video', 'tagged_cars')  # Prevent user and video from being editable


class CarVideoDeleteForm(CarVideoBaseForm):
    pass
