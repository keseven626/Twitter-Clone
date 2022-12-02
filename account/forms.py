from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class UserProfileForm(forms.ModelForm):
    Date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)
    job = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Hobbies = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    Bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    class Meta:
        model = Profile
        fields = ('image', 'Date_of_birth', 'job', 'Hobbies', 'Bio')