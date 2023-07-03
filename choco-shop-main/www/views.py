from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from . import forms
from .models import (
    User,
    Chocolate,
    Order,
    images_path,
    City
)
from django.conf import settings


def redirect(request):
    return HttpResponseRedirect(reverse('catalog'))


def catalog(request):
    chocolates = Chocolate.objects.all()
    context = {
        'catalog': chocolates
    }

    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.pk)
        context = {
            'catalog': chocolates,
            'user': user
        }

    return render(request, 'www/index.html', context)


@login_required(login_url="/sign_in/")
def create_order(request, pk):

    user = User.objects.get(pk=request.user.pk)
    cities = City.objects.all()
    chocolate = Chocolate.objects.get(pk=pk)
    context = {
        'user': user,
        'cities': cities,
        'chocolate': chocolate
    }
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            address = request.POST['address']
            city = request.POST['city']
            price = request.POST['price']

            order = Order.objects.create(
                user=user,
                city=city,
                street=address,
                email=email,
                first_name=first_name,
                last_name=last_name,
                chocolate=chocolate,
                total_price=price
            )
            order.save()
            context = {
                'order': order,
                'chocolate': chocolate
            }
            return render(request, 'www/order_detail.html', context)
        except:
            return HttpResponse(status=500)

    return render(request, 'www/order.html', context)


def sign_user(request):

    error = False
    context = {'error': error}

    if request.method == 'POST':
        try:
            username = request.POST['login']
            password = request.POST['passw']
            users = User.objects.all()
            user = None
            for i in users:
                if i.username == username and i.password == password:
                    user = i
            if user:
                print(user.first_name)
                login(request, user)
                return redirect("catalog")
        except:
            error = True
            context = {'error': error}

    return render(request, "www/login.html", context)


def register_user(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['login']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['passw']
        password_repeat = request.POST['passw_repeat']
        if password != password_repeat:
            return render(request, "www/registration.html", {'error': True})

        new_user = User.objects.create(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        new_user.save()
        return redirect('catalog')
    return render(request, "www/registration.html", {'error': False})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("catalog")




