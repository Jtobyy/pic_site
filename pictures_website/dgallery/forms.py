from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image


class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ImageForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control '}))
