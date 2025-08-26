from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url=("signin"))
def home(request):
    return render(request,("home.html"))

def signup(request):
    if request.method=='POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 != pass2:
            return HttpResponse("Your password and the confirm password are not same!!")
        else:
            user = User.objects.create_user(username,email,pass1)
            user.save()
            return redirect('signin')        
    
    return render(request,("signup.html"))


def signin(request):
    if request.method=='POST':
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        users = authenticate(request,username=username,password=pass1)
        if users is not None:
            login(request,users)
            return redirect("home")
        else:
            return HttpResponse("Username or Password is invalid")
            
    return render(request,("signin.html"))

@login_required(login_url="signin")
def Logout(request):
    logout(request)
    return redirect("signin")
