from django.shortcuts import render
from notes import forms
# Create your views here.
def index(request):
    return render(request, 'notes/index.html')

def register(request):

    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form().save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'notes/registration.html',{'user_form':user_form,
                                                     'registered':registered})            
