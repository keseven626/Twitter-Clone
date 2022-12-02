from django.contrib import admin
from .models import Profile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Profile)