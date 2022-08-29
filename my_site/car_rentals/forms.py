from django import forms
from .models import Review
from django.forms import ModelForm

'''
class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email Address", max_length=50)
    review = forms.CharField(
        label="Your comments go here", 
        max_length=500,
        widget=forms.Textarea(attrs={
            'class':'myform', 
            'rows':'12',
            'cols':'25'})
        )

'''

class ReviewForm(ModelForm):
    class  Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']
