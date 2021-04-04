from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_View(request,*args,**kwargs):
    return render(request,'home.html',{})

def main_view(request, *args,**kwargs):
    return HttpResponse(request,'books/main_book_view.html',{})

def login_view(request, *args,**kwargs):
    return render(request,'books/login.html',{})

def signup_view(request, *args,**kwargs):
    return render(request,'books/signup.html',{})