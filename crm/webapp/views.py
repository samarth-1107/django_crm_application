from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.core.paginator import Paginator

# LANDING PAGE : 
def home(request):
    return render(request,'webapp/index.html')

# USER DASHBOARD : 

@login_required(login_url='login')
def dashboard(request):
    admin_records = Record.objects.all()
    paginator = Paginator(admin_records,5)
    page_number=request.GET.get('page')
    final_admin_records = paginator.get_page(page_number)
    total_pages = final_admin_records.paginator.num_pages
    context = {
        'admin_records':final_admin_records,
        'total_page_list':[n+1 for n in range(total_pages) ]
        }
    return render(request,'webapp/user/dashboard.html', context=context)

# CREATE A RECORD
@login_required(login_url='login')
def create_record(request):
    create_record_form = CreateRecordForm()
    if request.method == "POST":
        create_record_form = CreateRecordForm(request.POST)
        if create_record_form.is_valid():
            create_record_form.save()
            return redirect("dashboard")
    context = {'create_record_form':create_record_form}
    return render (request, 'webapp/user/create-record.html', context=context)

# UPDATE RECORD
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    update_record_form = UpdateRecordForm(instance=record)
    if request.method=="POST":
        update_record_form = UpdateRecordForm(request.POST, instance=record)
        if update_record_form.is_valid():
            update_record_form.save()
            return redirect("dashboard")
    context = {'update_record_form':update_record_form}
    return render (request, 'webapp/crud/update-record.html', context=context)

# VIEW A RECORD : 
@login_required(login_url='login')
def view_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {'record': all_records}
    return render (request, 'webapp/crud/view-record.html', context=context)

# DELETE RECORD : 
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect ('dashboard')

# USER AUTHENTICATION
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
                return redirect('dashboard')
    context = {'login_form': login_form}
    return render (request, 'webapp/user/login.html', context=context)

def logout(request):
    auth.logout(request)
    return redirect('home')
    


