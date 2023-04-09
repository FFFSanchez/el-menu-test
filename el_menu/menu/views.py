from django.shortcuts import render


def home(request, pk=None):
    context = {}
    return render(request, 'menu/home.html', context)
