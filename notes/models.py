from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#storing user profile data
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#storing posts in the databse
class notes(models.Model):
    tag = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.notes.tag

#For Commenting on any post it will require login
class comments(models.Model):
    name = models.CharField(blank = True ,max_length = 50)
    post_comment = models.CharField(blank = True , max_length = 200)

#For storing Feedback from any visitors
class Feedback(models.Model):
    feedback_name = models.CharField(max_length = 50)
    feedback_comment = models.TextField(max_length = 200)
