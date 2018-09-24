from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    #path('user_login/',views.UserLoginView.as_view(),name='user_login'),
    path('user_logout/',views.LogoutView.as_view(),name='logout'),
    path('register/',views.register,name='register'),
    path('django_notes/',views.django_notes,name = 'django_notes'),
    path('python_notes/',views.python_notes,name = 'python_notes'),
    path('java_notes/',views.java_notes,name = 'java_notes'),
    path('javascript_notes/',views.javascript_notes,name = 'javascript_notes'),
    path('mysql_notes/',views.mysql_notes,name = 'mysql_notes'),
    path('machine_learning_notes/',views.machine_learning_notes,name = 'machine_learning_notes'),
    path('front_end_notes/',views.front_end_notes,name = 'front_end_notes'),
    path('c_notes/',views.c_notes,name = 'c_notes'),

]
