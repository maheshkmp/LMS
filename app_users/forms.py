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

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types = [
        (student, 'student'),
        (parent, 'parent'),
    ]

user_type = forms.ChoiceField(required=True, choices=user_types)

class Meta():
    model = userProfileInfo
    fields = ('bio', 'profile_pic', 'user_type')


