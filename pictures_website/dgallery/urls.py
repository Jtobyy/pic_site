from django.urls import path
from . import views

app_name = "dgallery"

urlpatterns = [
    path('', views.login_view, name = 'login'),    
    path('profile', views.profile, name = 'profile'),
    path('addimage', views.imageformview, name = 'imageform'),
    path('register', views.register, name = 'register'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
]