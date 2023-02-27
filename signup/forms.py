from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','profile_pic','username','email','password1', 'password2', 
                  'address_line1', 'address_city', 'address_state', 'address_pincode', 'user_type']
        
class LoginForm(forms.Form):

    USERTYPE_CHOICES = (
    ("-----", "-----"),
    ("Patient", "Patient"),
    ("Doctor", "Doctor")
    )

    user_type = forms.ChoiceField(choices=USERTYPE_CHOICES,initial='-----')
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput())