from django.shortcuts import render, redirect
from users.forms import UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def create_user(request):
    form = UserModelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/books')
    return render(request, 'register.html', {'form': form})

def do_login(request):
    form = UserModelForm(request.POST or None)
    error = ''

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    login(request, user)
                    return redirect('/books')
                except:
                    error = 'Internal error'
            else:
                error = 'Inactive user'
        else:
            error = 'User or password invalid!'

    return render(request, 'login.html', {'form': form, 'error': error})

def do_logout(request):
    logout(request)
    return redirect('/')
