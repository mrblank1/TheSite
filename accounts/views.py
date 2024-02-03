from django.shortcuts import render ,redirect
from django.contrib.auth import   login ,logout ,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserCreationForm ,EmailOrUsernameAuthenticationForm
from django.urls import reverse 
from django.contrib import messages
from django import forms
# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form=AuthenticationForm(request=request , data=request.POST)
#             if form.is_valid():
#                 username=form.cleaned_data.get('username')
#                 password=form.cleaned_data.get('password')
#                 authenticate=EmailOrUsernameModelBackend.authenticate()
#                 user=authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)    
#                 return redirect('/')
#         form=AuthenticationForm()
#         context={'form': form}
#     else:
#         return redirect('/')
    
#     context={'form': form}

#     return render(request,'accounts/login.html',context)
def log_view(request):
    if not request.user.is_authenticated and request.POST.get('form_name') == 'form':
        if request.method == 'POST':
            form = EmailOrUsernameAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(request, **form.cleaned_data)
                if user is not None:
                    login(request, user)
                    return redirect('/')
    if request.user.is_authenticated:
        messages.add_message(request, messages.INFO , "your already logged in")   
    form = EmailOrUsernameAuthenticationForm()
    form1 = UserCreationForm()
    if not request.user.is_authenticated and request.method == 'POST' and request.POST.get('form_name') == 'form1':
        form1 = UserCreationForm(request.POST,request=request)
        if form1.is_valid():
            form1.save()
            messages.success(request, "Registration successful")
            return redirect('/')  # Adjust the URL as needed
        else:
            messages.error(request, "Form is not valid. Please correct the errors.")
    elif request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")

    
    
    context = {'form': form, 'form1': form1}
    return render(request, 'accounts/login-register.html', context)
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

# def signup_view(request):
#     if not request.user.is_authenticated and request.method == 'POST' and request.POST.get('form_name') == 'form1':
#         form1 = UserCreationForm(request.POST)
#         if form1.is_valid():
#             form1.save()
#             messages.success(request, "Registration successful")
#             return redirect('/')  # Adjust the URL as needed
#         else:
#             messages.error(request, "Form is not valid. Please correct the errors.")
#     elif request.user.is_authenticated:
#         messages.warning(request, "You are already logged in.")
#     else:
#         form1 = UserCreationForm()
#     context = {'form1': form1}
#     return render(request, 'accounts/login-register.html', context)
   
# Create your views here.
