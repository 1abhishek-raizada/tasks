from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
#class tasking(UserCreationForm):
#    email=forms.EmailField()
 #   class Meta:
#        model=Task
#        fields=['username','email','pass1','pass2']
class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields=['description','image']