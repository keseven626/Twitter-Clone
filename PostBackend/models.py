from django.contrib.auth.models import User
from django.db import models

# Create your models here.
    
class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True,blank=True, on_delete=models.SET_NULL, related_name="retweet")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='tweet_image', null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='tweetLike')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.tweet
    
    @property 
    def is_retweet(self):
        return self.parent != None
    
    
    class Meta:
        ordering = ['-date_created']
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='comment', on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    likes = models.ManyToManyField(User, related_name='CommentLike', blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content