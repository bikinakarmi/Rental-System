from django import  forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Property

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('title', 'description', 'location', 'picture','price', 'area', 'property_type')