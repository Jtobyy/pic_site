from django.contrib import messages
from django.contrib.messages.constants import ERROR, SUCCESS
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegForm, ImageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Image, ProfileInfo
from django.contrib.auth.models import User

@login_required(login_url='/dgallery/login')
def homepage(request):
    image_objects = Image.objects.all()
    profileimages = ProfileInfo.objects.all()
    users = User.objects.all()
    userprofile = ProfileInfo.objects.get(user=request.user)
    context = {
        'image_objects': image_objects,
        'profiles': profileimages,
        'users': users,
        'userprofile': userprofile
    }
    return render(request, 'dgallery/homepage.html', context)

@login_required(login_url='/dgallery/login')
def profile(request):
    image_objects = Image.objects.filter(user=request.user)
    profile_object = ProfileInfo.objects.filter(user=request.user)    
    # print("profile object is {}".format(profile_object))
    if len(profile_object) != 0:
        if len(image_objects) == 1:
            posts = f'1 post'
        else:
            posts = f'{len(image_objects)} posts'
        context = {
            'image_objects': image_objects,
            'username': request.user.username,
            'profileinfo': profile_object,
            'posts': posts
        }    
    else:
        context = {
            'image_objects': image_objects,
            'username': request.user.username,
    }
    return render(request, 'dgallery/profilepage.html', context)

@login_required(login_url='dgallery/login')
def addprofileimageview(request):
    if request.method == 'POST':
        profimg = request.FILES['image']
        prevprofimg = ProfileInfo.objects.filter(user=request.user)
        if (len(prevprofimg) != 0):
            prevprofimg[0].profileimage = profimg
            prevprofimg[0].save()
        else:
            prof_ins = ProfileInfo(profileimage=profimg)     
            prof_ins.user = request.user
            prof_ins.save()
        messages.add_message(request, messages.SUCCESS, "profile image updated")
        return redirect("/dgallery/profile", permanent=True)
    else:
        image_objects = Image.objects.filter(user=request.user)
        profile_object = ProfileInfo.objects.filter(user=request.user)    
        form = ImageForm()
        if len(profile_object) != 0:
            if len(image_objects) == 1:
                posts = f'1 post'
            else:
                posts = f'{len(image_objects)} posts'
            context = {
                'image_objects': image_objects,
                'username': request.user.username,
                'profileinfo': profile_object,
                'posts': posts,
                'form': form
            }    
        else:
            context = {
                'image_objects': image_objects,
                'username': request.user.username,
                'form': form
            }
        return render(request, 'dgallery/profilepopup.html', context)

@login_required(login_url='dgallery/login')
def editbioview(request):
    if request.method == 'POST':
        bio = request.POST['caption']
        prevprofbio = ProfileInfo.objects.filter(user=request.user)
        if (len(prevprofbio) != 0):
            prevprofbio[0].bio = bio
            prevprofbio[0].save()
        else:
            prof_ins = ProfileInfo(bio=bio)   
            prof_ins.user = request.user
            prof_ins.save()
        print(prevprofbio[0])
        return redirect("/dgallery/profile", permanent=True)
    
    else:
        image_objects = Image.objects.filter(user=request.user)
        profile_object = ProfileInfo.objects.filter(user=request.user)    
        form = ImageForm()
        if len(profile_object) != 0:
            if len(image_objects) == 1:
                posts = f'1 post'
            else:
                posts = f'{len(image_objects)} posts'
            context = {
                'image_objects': image_objects,
                'username': request.user.username,
                'profileinfo': profile_object,
                'posts': posts,
                'form': form
            }
        else:
            context = {
                'image_objects': image_objects,
                'username': request.user.username,
                'form': form
            }
        return render(request, 'dgallery/bioform.html', context)    

@login_required(login_url='/dgallery/login')
def imageformview(request):    
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            img = image_form.cleaned_data.get("image")
            capt = image_form.cleaned_data.get("caption")
            img_ins = Image(image=img, caption=capt, date_added=timezone.now())
            img_ins.user = request.user
            img_ins.save()
            return redirect("/dgallery/profile", permanent=True)
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
                return redirect("/dgallery/", permanent=True)
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