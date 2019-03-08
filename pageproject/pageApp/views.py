from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,"pageApp/index.html")


def page1(request):
    return render(request,"pageApp/page1.html")


def page2(request):
    return render(request,"pageApp/page2.html")


def page3(request):
    return render(request, "pageApp/page3.html")