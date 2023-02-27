from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def RegisterView(request):

    try:

        form = RegisterForm()
        if request.method == "POST":
           form = RegisterForm(request.POST, request.FILES)
           if form.is_valid():
              instance = form.save()
              user_type = form.cleaned_data.get('user_type')
              first_name = form.cleaned_data.get('first_name')
              last_name= form.cleaned_data.get('last_name')
              profile_pic = form.cleaned_data.get('profile_pic')
              username= form.cleaned_data.get('username')
              email = form.cleaned_data.get('email')
              password = form.cleaned_data.get('password')
              address_line1 = form.cleaned_data.get('address_line1')
              address_city= form.cleaned_data.get('address_city')
              address_state = form.cleaned_data.get('address_state')
              address_pincode= form.cleaned_data.get('address_pincode')

              messages.success(request, "User Registeration Successful.")
              return redirect('register')

        context ={'form': form}
        return render(request,"register.html", context)
    except Exception as e:
        return HttpResponse(e)

def LoginView(request):
    try:
        form = LoginForm()
        if request.method =="POST":
            form = LoginForm(request.POST)
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home', kwargs={"pk": user.id}))
            else:
                messages.error(request, "Authentication Failed!")

        context = {'form': form}
        return render(request,"login.html", context)
    except Exception as e:
        return HttpResponse(e)
    

@login_required
def HomeView(request, pk):
    user = User.objects.get(id=pk)
    return render(request,'home.html',{'user': user})


def LogoutView(request):
    logout(request)
    return redirect('login')