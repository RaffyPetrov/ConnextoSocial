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


class CarVideoEditForm(forms.ModelForm):
    class Meta:
        model = CarVideo
        exclude = ['video']  # Exclude the video field for editing if necessary


class CarVideoDeleteForm(CarVideoBaseForm):
    pass



