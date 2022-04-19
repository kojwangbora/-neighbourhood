from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, NeighbourHood, Business,Post


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

    class Meta:
        model = NeighbourHood
        fields = '__all__'
        exclude=['user']
    
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'hood')
