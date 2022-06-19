from django.shortcuts import render,redirect
from .models import Reader,City
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('home')


def login(request):
    if request.method == 'POST':
        user=auth.authenticate(request,
        username=request.POST['readerID'],
        password=request.POST['password'])
        print(user)
        if user is None:
            messages.error(request,'Invalid CREDENTIALS')
            return redirect('/Reader/login/')
        else:
            auth.login(request,user)
            messages.success(request, 'Login Successful')
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
    else:
        return render(request, 'Reader/login.html')


def signup(request):

    if request.method=='POST':
        try:
            user=User.objects.get(username=request.POST['readerID'])
            messages.success(request, 'user exits already!!')
            return redirect('/Reader/login/')

        except User.DoesNotExist:
            user=User.objects.create_user(username=request.POST['readerID'],
            password=request.POST['password'])

            newreader=Reader.objects.create(first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            city=City.objects.get(id=request.POST['city']),reader_id=user)

            auth.login(request,user)
            messages.success(request, 'Signup Successful')
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')

    else:
        return render(request, 'Reader/signup.html',{"city":City.objects.all(),
        "users":list(User.objects.values_list('username',flat=True))
        })

