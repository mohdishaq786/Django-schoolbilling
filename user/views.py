from http.client import HTTPResponse
from unittest.util import _MAX_LENGTH
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import UserEnrollmentForm
from django.contrib import messages
from datetime import datetime
from user.models import contact


def register(request):
    if request.method == 'POST':
        form = UserEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserEnrollmentForm()
    return render(request, 'users/enrollment.html', {'form':form, 'title': 'Enrollment'})


def home(request):
    return render(request, 'posts/home.html')

def about(request):
    return render(request, 'posts/aboutus.html')
def login(request):
    return render(request, 'posts/login.html')
def defaultor(request):
    return render(request, 'posts/Defaultorlist.html')

def contact(request):
    if request.method == "POST" :
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contacts=contact( name=name,email=email,phone=phone,desc=desc )
        contacts.save()
    return render(request, 'posts/contactus.html')