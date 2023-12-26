from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

def home(request):
    return render(request,'webapp/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('')
    context = {'form':form}
    return render(request,'webapp/user/register.html', context=context)

def login(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form=LoginForm(request, data = request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None :
                auth.login(request, user)
                # return redirect('')
    context = {'login_form': login_form}
    return render (request, 'webapp/user/login.html', context=context)
    


