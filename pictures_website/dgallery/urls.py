from django.urls import path
from . import views

app_name = "dgallery"

urlpatterns = [
    path('login', views.login_view, name = 'login'),
    path('register', views.register, name = 'register'),
]