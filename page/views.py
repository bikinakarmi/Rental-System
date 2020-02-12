from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request,'index.html')

def signup(request):
    return render(request, 'registration/signup.html')

def login(request):
    return render(request, 'registration/login.html')