from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, NeighbourHood
from cloudinary.models import CloudinaryField


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required.enter a valid email!')


    class Meta:
        model = User
        fields=('username', 'email', 'password1','password2')
    

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','neighbourhood')

class NeighbourHoodForm(forms.ModelForm):
    photo = CloudinaryField(label='')

    class Meta:
        model = NeighbourHood
        fields = ('logo', 'name', 'location', 'description')
        exclude=['user']