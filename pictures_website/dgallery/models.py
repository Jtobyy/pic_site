from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return f'User_{instance.user.id}/{filename}'

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to = user_directory_path)
    caption = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=False)
