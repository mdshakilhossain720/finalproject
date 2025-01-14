from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegestionForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confrim Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','email','password','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        
