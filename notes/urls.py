from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    #path('user_login/',views.UserLoginView.as_view(),name='user_login'),
    path('user_logout/',views.LogoutView.as_view(),name='logout'),

    path('register/',views.register,name='register'),

]
