from django.contrib import admin
from notes.models import notes,UserProfileInfo,comments,Feedback

# Register your models here.
admin.site.register(notes)
admin.site.register(UserProfileInfo)
admin.site.register(comments)
admin.site.register(Feedback)
