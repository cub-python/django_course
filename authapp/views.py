from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfilerForm
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        # else:
        #     print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Geekshop | Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop | Регистрация',
        'form': form}
    return render(request, 'authapp/register.html', context)

@login_required         #обьявили декоратор,он даст воможность перенаправления
def profile(request):
    if request.method == 'POST':
       form = UserProfilerForm(instance=request.user,data=request.POST,files=request.FILES)
       if form.is_valid():
           messages.success(request, 'Вы успешно сохранили профайл')
           form.save()
       else:
           print(form.errors)

    total_quahtity = 0
    total_sum = 0
    baskets = Basket.objects.filter(user=request.user)
    for basket in baskets:
        total_quantity += basket.quantity
        total_sum = basket.sum()

    context = {
        'title': 'Geekshop | Профайл',
        'form' : UserProfilerForm(instance=request.user),
        'baskets': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')