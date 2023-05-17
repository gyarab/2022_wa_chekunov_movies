from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CommentForm(forms.Form):
    author = forms.CharField(required=False)
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 2}))
    rating = forms.IntegerField(required=False, max_value=100,min_value=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )