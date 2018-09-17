from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_site = models.URLField(blank=True,)
    profile_pic = models.ImageField(upload_to="profile_pic",)

class notes(models.Model):
    tag = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.notes.tag
