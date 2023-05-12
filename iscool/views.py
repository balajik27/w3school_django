import http
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from .forms import custom

def index(request):
    myform = custom()
    return render(request, 'index.html',{'form':myform})

def home():
    return HTTPResponse("hello world")

def about():
    return HTTPResponse("about page")

def login():
    return HTTPResponse("login")