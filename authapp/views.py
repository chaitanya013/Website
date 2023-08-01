from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def signup(request):

    if request.method=="POST":
        get_email= request.POST.get('email')
        get_pass= request.POST.get('pass1')
        get_confirm_pass= request.POST.get('pass2')
        if get_pass!=get_confirm_pass:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup/')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,'Email already taken')
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        myuser= User.objects.create_user(get_email,get_email,get_pass)
        myuser.save()
        myuser = authenticate(username=get_email, password=get_pass)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, 'User Created & Login success')
            return redirect('/')

    return render(request, 'signup.html')

def Login(request):
    if request.method=="POST":
        get_email= request.POST.get('email')
        get_pass= request.POST.get('pass1')
        myuser= authenticate(username=get_email,password=get_pass)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login success')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
    return render(request, 'login.html')
def Logout(request):
    logout(request)
    messages.success(request,'Logout success')
    return render(request, 'login.html')