from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from web.forms import *
from web.models import *

@login_required
def main_view(request):
    news = News.objects.all()

    return render(request, "web/main.html", {
        'news': news
    })

def news_add_view(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(data=request.POST, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "web/news_create.html", {
        "form": form
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )

            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, "web/registration.html", {
        "form": form,
        "is_success": is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Неправильный логин или пароль")
            else:
                login(request, user)
                return redirect("main")
    return render(request, 'web/auth.html', {
        "form": form
    })


def logout_view(request):
    logout(request)
    return redirect("main")
