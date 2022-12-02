from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('tweet/<str:pk>', getTweet, name='getTweet'),
    path('create-tweet/', CreateTweet, name='create-tweet'),
    path('re-tweet/<str:pk>/', Retweet, name='re-tweet'),
    path('like/<str:pk>', likeComment, name='like-comment'),
    path('like/tweet/<str:pk>', likeTweet, name='like-tweet')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
