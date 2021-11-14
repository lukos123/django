from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def index(request):
    P = Posts.objects.all()
    adm = False
    if request.user.is_superuser:
        adm = True

    return render(request, 'women/index.html', {'post': P, 'adm': adm})


def public(request, num=-1):
    adm = False
    if request.user.is_superuser:
        adm = True
    if num != -1:
        P = Posts.objects.get(pk=num)

        return render(request, 'women/post.html', {'post': P, 'adm': adm})
    return redirect('home')
