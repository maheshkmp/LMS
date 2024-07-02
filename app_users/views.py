from django.shortcuts import render
from django.http import HttpResponse
from app_users.forms import UserForm, UserProfileInfoForm

# Create your views here.

def index(request):
    return HttpResponse('This is home page')

def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)