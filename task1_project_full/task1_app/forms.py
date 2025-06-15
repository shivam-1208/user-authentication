from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type',
                  'first_name', 'last_name', 'profile_picture',
                  'address_line1', 'city', 'state', 'pincode']
