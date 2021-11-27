from django.contrib import messages
from django.contrib.messages.constants import ERROR, SUCCESS
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegForm, ImageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import ImageForm
from .models import Image
from django.contrib.auth.models import User

@login_required(login_url='/dgallery/login')
def profile(request):
    return render(request, 'dgallery/profilepage.html', None)

@login_required(login_url='/dgallery/login')
def imageformview(request):    
    if request.method == 'POST':
        print(request.FILES)
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            img = image_form.cleaned_data.get("image")
            capt = image_form.cleaned_data.get("caption")
            img_ins = Image(image=img, caption=capt, date_added=timezone.now())
            img_ins.user = request.user
            img_ins.save()
            return HttpResponse("Image successfully added")
        else:
            messages.add_message(request, messages.ERROR, "Invalid details")
    else:
        image_form = ImageForm()
        return render(request, 'dgallery/imageform.html', {'image_form': image_form})
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            if request.POST['next']:
                next = request.POST['next']
        except UnboundLocalError:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Login successful")
            try:
                return redirect(next)
            except UnboundLocalError:
                return HttpResponse("Welcome")
    return render(request, 'dgallery/login.html', None)
        
def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Registration successful")
            return redirect("/dgallery/login", permanent=True)
        messages.add_message(request, messages.ERROR, "Invalid details")
    form = RegForm()
    return render (request, "dgallery/register.html", {'form': form})

def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logged Out")
    return redirect("/dgallery/login", permanent=True)