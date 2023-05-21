from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class CommentForm(forms.Form):
    author = forms.CharField(required=False,
    widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Autor"})
    )
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 2,"class": "form-control", "placeholder": "Very good.."}))
    rating = forms.IntegerField(required=False, max_value=100,min_value=1,
    widget=forms.NumberInput(attrs={"class":"form-control","type":"number","placeholder": "1-100"}),
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )