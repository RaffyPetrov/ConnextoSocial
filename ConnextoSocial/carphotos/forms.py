from django import forms

from ConnextoSocial.carphotos.models import CarPhoto


class CarPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = CarPhoto
        exclude = ('user', )


class CarPhotoAddForm(CarPhotoBaseForm):
    pass


class CarPhotoEditForm(forms.ModelForm):
    class Meta:
        model = CarPhoto
        exclude = ['photo']


class CarPhotoDeleteForm(CarPhotoBaseForm):
    pass
