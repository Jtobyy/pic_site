from django.db import models
from django.contrib.auth.models import User

def user_directory_path(User, filename):
    return f'User_{User.id}/{filename}'

class Image(models.Model):
    image = models.ImageField(upload_to = user_directory_path)
    caption = models.TextField()
    date_added = models.DateTimeField(auto_now_add=False)
