from django import forms

from ConnextoSocial.cars.models import Cars


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['car_name', 'year_of_production', 'car_model',]

        widgets = {
            'car_name': forms.TextInput(attrs={'placeholder': 'Car name'}),
            'year_of_production': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Year of production'}),
            'car_model': forms.TextInput(attrs={'placeholder': 'Car Model'}),
        }

        labels = {
            'car_name': 'Car Name',
            'year_of_production': 'Year of production',
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
