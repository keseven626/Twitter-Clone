from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from account.models import Profile
from PostBackend.forms import TweetForm
from PostBackend.models import Comment, Tweet


# Create your views here.
def Home(request):
    if request.user.id: 
        tweet = Tweet.objects.all()
        profile = Profile.objects.get(user=request.user)
    else:
        tweet = Tweet.objects.all()
        profile = False
    context={'tweet': tweet, 'profile': profile}
    return render(request, 'home/Homepage.html', context)

def CreateTweet(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form': form}
    return render(request, 'home/createTweet.html', context)

def Retweet(request, pk):
    obj = Tweet.objects.get(id=pk)
    tweet = Tweet.objects.create(
        user=request.user,
        tweet=obj.tweet,
        image=obj.image,
        parent=obj
    )
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def getTweet(request, pk, **kwargs):
    tweet = Tweet.objects.get(id=pk)
    comment = tweet.comment.all()
    if request.method == 'POST':
        tweet.likes.add(request.user)
    context={'tweet': tweet, 'comment': comment}
    return render(request, 'home/getTweet.html', context)

def likeComment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
       comment.likes.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def likeTweet(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    if tweet.likes.filter(id=request.user.id).exists():
        tweet.likes.remove(request.user)
    else:
       tweet.likes.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])