from django.shortcuts import render
from django.utils import timezone
from notes.forms import UserForm,notes_form
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

def index(request):
    return render(request, 'notes/index.html')

def file_python(request):
    note_python = notes.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'notes/file_python.html',{'note_python':note_python})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = User.objects.create_user(username=request.POST['username'],
                                            email=request.POST['email'],
                                            password=request.POST['password'])
            # user.save()
            # user.set_password(user.password)

            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'notes/registration.html',{'user_form':user_form,
                                                     'registered':registered})

def user_login(request):
    print(request, request.method)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print("login successful")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("account not active")
        else:
            print("login failed for {}".format(username))
            return HttpResponse("invalid login credentials !!")
    return render(request, 'notes/login.html')
from django.contrib.auth.views import LoginView, LogoutView


# class UserLoginView(LoginView):
#     template_name = 'notes/login.html'



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('logout'))
