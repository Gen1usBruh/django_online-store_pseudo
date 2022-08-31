from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login', views.login, name='login-page'),
    path('register', views.register, name='register-page'),
    path('profile', views.profile, name='profile-page'),
    path('logout', views.logout_view, name='logout_user')

]
