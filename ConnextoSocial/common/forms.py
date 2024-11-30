from django import forms

from ConnextoSocial.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment'}),
        }


class SearchForm(forms.Form):
    car_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by car name'
            }
        )
    )
