from django.shortcuts import render

def login(request):
    return render(request, 'dgallery/index.html', None)

def register(request):
    pass
