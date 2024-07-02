from django import forms
from django.contrib.auth.models import User
from app_users.models import userProfileInfo

class UserForm(UserCreationform):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'mail', 'password')

        labels = {
            'password1' : 'Password',
            'password2' : 'Confirm Password'
        }


