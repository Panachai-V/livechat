from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.template import RequestContext
from redischatapp.models import Profile

def home(request):
    return render(request,'home.html')

def redislogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        #show error
        return render(request,'login.html',
        {'error':'Your username or password are incorrect',
        'urlregister':resolve_url('redisregister'),
        'urllogin':resolve_url('redislogin')})

def redislogout(request):
    # context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return redirect('index')

def redisregister(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        email = request.POST.get("email", "")
        name = request.POST.get("name","")
        if not User.objects.filter(username=username).exists():
            User1=User.objects.create(username=username,email=email)
            User1.set_password(password)
            User1.save()
            userprofile= Profile.objects.get(user=User1)
            userprofile.Name=name
            userprofile.save()
            return render(request,'login.html',{'submit':'Sign up success'})
        else:
            return render(request,'register.html',{'error':'Your username is already exist.'})
    else:
        return render(request, 'register.html')
