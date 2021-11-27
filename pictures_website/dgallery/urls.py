from django.urls import path
from . import views

app_name = "dgallery"

urlpatterns = [
    path('', views.login_view, name = 'login'),    
    path('profile', views.profile, name = 'profile'),
    path('addimage', views.imageformview, name = 'imageform'),    
    path('login', views.login_view, name = 'login'),
    path('register', views.register, name = 'register'),
]