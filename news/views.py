from django.shortcuts import render
from django.http import HttpResponse


def news_home(request):
    return render(request, 'news/index.html')
