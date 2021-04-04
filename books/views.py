from django.shortcuts import render
from .models import books

def genre_detail_view(request):
    #ignore this error
    obj_list=[]
    for i in range(1,25):
        if i not in [2,3]:
            obj_list.append(books.objects.get(id=i))

    context={
        'object':obj_list
    }
    return render(request,'books/display_genres.html',context)
    
def Home_View(request,*args,**kwargs):
    return render(request,'home.html',{})

def main_view(request, *args,**kwargs):
    return HttpResponse(request,'books/main_book_view.html',{})

def login_view(request, *args,**kwargs):
    return render(request,'books/login.html',{})

def signup_view(request, *args,**kwargs):
    return render(request,'books/signup.html',{})
# def login_view(request):
#     return render(request,'templates/login.html',{})

# def signup_view(request):
#     return render(request,'templates/signup.html',{})