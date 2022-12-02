from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    Date_of_birth = models.DateField(blank=True, null=True)
    job = models.CharField(max_length=500, blank=True, null=True)
    Hobbies = models.CharField(max_length=500, blank=True, null=True)
    Bio = models.CharField(max_length=500, blank=True, null=True)
    follower = models.ManyToManyField(User, related_name="following", blank=True)
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def Create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def Save_User_profile(sender, instance, **kwargs):
    instance.profile.save()