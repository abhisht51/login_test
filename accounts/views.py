from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse


# Create your views here.


# def register(request):
#     if request.method == 'POST':
#         #getting values
#         firstname = request.POST['firstname']
#         lastname = request.POST['lastname']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
#         #password validation
#         if password == cpassword:
#            # Check username
#             if User.objects.filter(username=username).exists():
#                messages.error(request, 'That username is taken')
#                return redirect('register')
#             else:
#                if User.objects.filter(email=email).exists():
#                   messages.error(request, 'That email is taken')
#                   return redirect('register')
#                else:                   
#                   user = User.objects.create_user(username=username, password=password,email=email,firstname=firstname,lastname=lastname)
#                     #  auth.login(request, user)
#                   #   messages.success(request, 'You are now logged in')
#                   #   return redirect('index')
#                   user.save()
#                   messages.success(request, 'You are now registered and can log in')
#                   return redirect('login')
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')
#     else:
#         return render(request, 'accounts/register.html')


def register(request):
    #print(request.data)
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    #subscription_period = request.data.get('subscription_period')

    user = User.objects.create_user(email = email, password = password)
    user.first_name = first_name
    user.last_name = last_name
    #user.subscription_period = subscription_period
    user.save()

    # Generate Token for user
    token = Token.objects.create(user=user)

    logged_in_user = User.objects.filter(email = user).values()[0]

    return JsonResponse({'status': 'success', 'token': token.key, 'user_data': {
        'email': logged_in_user.get('email'),
        'first_name': logged_in_user.get('first_name'),
        'last_name': logged_in_user.get('last_name'),
        # 'subscription_period': str(logged_in_user.get('subscription_period')),
        # 'subscription_end': str(logged_in_user.get('subscription_end')).split(" ")[0]
    }})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login ')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def home(request):
    return render(request, 'accounts/home.html')
    # define schemas for events / databases for culturall technical and everything 
    # working database plus api calls 
    # cultural.objects.all() - will give a list of query items with in json formats 
    # 