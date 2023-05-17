from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CommentForm(forms.Form):
    author = forms.CharField(required=False,
    widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Evžen"})
    )
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 2,"class": "form-control", "placeholder": "Very good.."}))
    rating = forms.IntegerField(required=False, max_value=100,min_value=1,
    widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "1-100","type":"number"}),
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )