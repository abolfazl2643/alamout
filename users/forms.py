from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_Creation_Form(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','password1','password2')

class User_Update_Form(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = User
        fields = ('username',)
