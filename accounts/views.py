from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
# Create your views here.


def sign_up_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')

    form = UserCreationForm()
    context = {
        'form':form,
    }

    return render(request,'accounts/sign_up.html',context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('orders:home')
        
    form = AuthenticationForm()
    context = {
        'form':form
    }

    return render(request, 'accounts/login.html',context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')




