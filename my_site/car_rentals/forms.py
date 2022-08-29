from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email Address", max_length=50)
    review = forms.CharField(
        label="Your comments go here", 
        max_length=500,
        widget=forms.Textarea(attrs={'class':'myform', 'rows':'12','cols':'25'})
        )

