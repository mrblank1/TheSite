from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import password_validation
from captcha.fields import CaptchaField
class UserCreationForm(UserCreationForm):
    captcha = CaptchaField()

    email = forms.EmailField(required=True, label='Email')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Get the 'request' parameter
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            messages.add_message(self.request, messages.INFO , "user exists")   
           
            raise forms.ValidationError("This username is already taken. Please choose a different one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            messages.add_message(self.request, messages.INFO , "email exists")   

            raise forms.ValidationError("This email address is already registered. Please use a different one.")
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            messages.add_message(self.request, messages.INFO , "password mismatch")   
        else:
            try:
                password_validation.validate_password(password1, self.instance)
            except :
                if self.request:
                    messages.add_message(self.request, messages.INFO ,"Password is not strong enough. Please choose a stronger password.")
        return password2
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    captcha = CaptchaField()
    username=forms.CharField(label='Username or Email')
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' in username:
            try:
                user = User.objects.get(email=username)
                return user.username
            except User.DoesNotExist:
                pass
        return username

