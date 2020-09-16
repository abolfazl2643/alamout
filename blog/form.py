from django import forms
from .models import Post,Comment
from django.db import models


class commentform(forms.ModelForm):

    class Meta:
        model = Comment      
        fields = ('author','massage')   
        widgets = {'author': forms.HiddenInput()}
        

