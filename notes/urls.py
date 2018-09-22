from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
<<<<<<< HEAD
    #path('user_login/',views.user_login,name='user_login'),
    path('user_login/',views.UserLoginView.as_view(),name='user_login'),
=======
    path('user_login/',views.user_login,name='user_login'),
    #path('user_login/',views.UserLoginView.as_view(),name='user_login'),
>>>>>>> 2ad5d675d0f3c37349432beb4754744a4f168e24
    path('user_logout/',views.LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),
    path('notes/',views.file_python,name = 'file_python'),

]
