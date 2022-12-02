from django.contrib import admin

from .models import *


# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    admin.site.register(Tweet)

class TweetAdmin(admin.ModelAdmin):
    list_display= ('user', 'comment')
    admin.site.register(Comment)

# class TweetAdmin(admin.ModelAdmin):
#     admin.site.register(Retweet)