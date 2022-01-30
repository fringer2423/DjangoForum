from django.shortcuts import render, redirect
from service.models import Post, Comment

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
