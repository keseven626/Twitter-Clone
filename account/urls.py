from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('login', UserLogin, name='login'),
    path('logout', UserLogout, name='logout'),
    path('register', UserRegistration, name='user-registration'),
    path('reset/password', ResetUserPassword, name='reset-user-password'),
    path('edit-profile', EditUserProfile, name='edit-profile'),
    path('user/profile/<str:pk>', UserProfile, name='profile'),
    path('follow/user/<str:pk>', followUser, name='follow'),
    path('un-follow/user/<str:pk>', followUser, name='un-follow'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)