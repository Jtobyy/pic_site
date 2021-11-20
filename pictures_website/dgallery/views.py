from django.conf.urls import url
from django.contrib import messages
from django.contrib.messages.constants import ERROR, SUCCESS
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, SUCCESS, "Login successful.")
            return HttpResponse("Thanks for testing")
    return render(request, 'dgallery/login.html', None)
        
def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.add_message(request, SUCCESS, "Registration successful.")
            return redirect("/dgallery/login", permanent=True)
        messages.add_message(request, ERROR, "Unsuccessful registration, Invalid information.")
    form = RegForm()
    return render (request, "dgallery/register.html", {'form': form})
