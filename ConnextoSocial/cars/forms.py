from django import forms

from ConnextoSocial.cars.models import Cars


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['car_name', 'car_photo', 'car_model']

        widgets = {
            'car_name': forms.TextInput(attrs={'placeholder': 'Car name'}),
            'personal_car_photo': forms.TextInput(attrs={'placeholder': 'Upload Image'}),
            'car_model': forms.TextInput(attrs={'placeholder': 'Car Model'}),
        }

        labels = {
            'car_name': 'Car Name',
            'personal_car_photo': 'Link to Image',
            'car_model': 'Car Model',
        }


class CarAddForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True