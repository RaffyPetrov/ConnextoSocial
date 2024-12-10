from django import forms
from ConnextoSocial.common.models import Comment, VideoComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Add comment'}),
        }


class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ['text']  # You only need the 'text' field from the VideoComment model
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': 'Add a comment...'})
        }


class SearchForm(forms.Form):
    car_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by car name'
            }
        )
    )


class CarVideoSearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by video title'
            }
        )
    )
