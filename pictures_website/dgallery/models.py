from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f'User_{instance.user.id}/{filename}'

def user_profile_path(instance, filename):
    return f'User_{instance.user.id}/profileimage/{filename}'

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to = user_directory_path)
    caption = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=False)

class ProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)    
    profileimage = models.ImageField(upload_to = user_profile_path)
    bio = models.CharField(max_length=100, null=True)
    date_updated = models.DateTimeField(auto_now_add=True)
