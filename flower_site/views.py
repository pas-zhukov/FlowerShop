from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def quiz(request):
    return render(request, 'quiz.html')


def catalogue(request):
    return render(request, 'catalog.html')