from django.urls import path
from . import views

app_name = "dgallery"

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('profile', views.profile, name = 'profile'),
    path('addimage', views.imageformview, name = 'imageform'),
    path('addprofileimage', views.addprofileimageview, name = 'profileimage'),
    path('editbio', views.editbioview, name = 'bio'),
    path('register', views.register, name = 'register'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
]