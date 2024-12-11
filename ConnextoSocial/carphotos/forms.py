from django import forms
from ConnextoSocial.carphotos.models import CarPhoto


class CarPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = CarPhoto
        exclude = ('user', )


class CarPhotoAddForm(CarPhotoBaseForm):
    pass


class CarPhotoEditForm(CarPhotoBaseForm):
    class Meta(CarPhotoBaseForm.Meta):
        exclude = ('user',)  # Prevent user from being editable


class CarPhotoDeleteForm(CarPhotoBaseForm):
    pass
