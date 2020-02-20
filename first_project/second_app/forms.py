from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)    

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']

        if(len(email) <= 20):
            raise(forms.ValidationError("NOPE"))