from django.contrib.auth import authenticate, login, logout
from .models import User
from chat.models import Group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


@login_required(login_url='/auth/login/')
def index(request):
    """Function to view groups"""
    try:
        group_list = (Group.objects.filter(user=request.user) | Group.objects.filter(members=request.user)).distinct()
        context = {'group_list': group_list}
        return render(request, 'index.html', context)

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


def register_user(request):
    """Function to register user details"""
    try:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone_no = request.POST['phone_no']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    return HttpResponse('Username is taken')
                else:
                    User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                             phone_no=phone_no, username=username, password=password1)
                    return redirect('login')
            return HttpResponse('Password is not matching')
        return render(request, 'user/registration.html')

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


def login_user(request):
    """Function to login the user"""
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            return HttpResponse('invalid credentials')
        return render(request, 'user/login.html')

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)


def logout_user(request):
    """Function to logout the user"""
    try:
        logout(request)
        return redirect('login')

    except Exception as e:
        logging.exception(e)
        return HttpResponse(e)
