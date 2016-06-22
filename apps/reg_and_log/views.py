from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    context = {
        'type' : True
    }
    print context['type']
    return render(request, 'reg.html', context)

def signin(request):
    context = {
        'type' : False
    }
    print context['type']
    return render(request, 'reg.html', context)

def create(request):
    results = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'], request.POST['user_level'])
    if not results[0]:
        print results[1]
        return HttpResponse('errors')
    else:
        print results[1]
        context = {
            'users' : User.objects.all()
        }
        return redirect('/signin')

def create_new(request):
    results = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['password_confirmation'], request.POST['user_level'])
    if not results[0]:
        print results[1]
        return HttpResponse('errors')
    else:
        print results[1]
        context = {
            'users' : User.objects.all()
        }
        return redirect('/dashboard/admin')

def login(request):
    results = User.userManager.login(request.POST['email'], request.POST['password'])
    if not results[0]:
        return HttpResponse('failed')
    else:
        request.session['id'] = results[1].id
        if (results[1].user_level >= 9):
            return redirect('/dashboard/admin')
        else:
            return redirect('/dashboard')

def logoff(request):
    request.session['id'] = 0;
    return redirect('/')
