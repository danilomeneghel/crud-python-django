from django.urls import path
from .views import do_login, do_logout, create_user

urlpatterns = [
    path('', do_login, name='login'),
    path('logout', do_logout, name='logout'),
    path('register', create_user, name='register'),
]
