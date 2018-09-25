from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#storing user profile data
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#storing posts in the databse
class notes(models.Model):

    PYTHON = 'PYTHON'
    DJANGO = 'DJANGO'
    JAVA = 'JAVA'
    MYSQL = 'MYSQL'
    MACHINE_LEARNING = 'MACHINE_LEARNING'
    JAVASCRIPT = 'JAVASCRIPT'
    FRONT_END = 'FRONT_END'
    C = 'C/C++'

    NOTE_CHOICE = (
        (PYTHON,'PYTHON'),
        (DJANGO,'DJANGO'),
        (JAVA,'JAVA'),
        (MYSQL,'MYSQL'),
        (MACHINE_LEARNING,'MACHINE_LEARNING'),
        (JAVASCRIPT,'JAVASCRIPT'),
        (FRONT_END,'FRONT_END'),
        (C,'C/C++')
    )

    author = models.CharField(max_length=100)
    tag = models.CharField(blank = True,choices = NOTE_CHOICE, max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#For Commenting on any post it will require login
class comments(models.Model):
    name = models.CharField(blank = True ,max_length = 50)
    post_comment = models.CharField(blank = True , max_length = 200)

#For storing Feedback from any visitors
class Feedback(models.Model):
    feedback_name = models.CharField(max_length = 50)
    feedback_comment = models.TextField(max_length = 200)
