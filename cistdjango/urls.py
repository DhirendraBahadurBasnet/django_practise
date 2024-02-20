
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from django.shortcuts import render
from random import randint


# def index(request):
#     # return HttpResponse(f"<h2>hello world , random num is {randint(0,10) }</h2>")
#     # username = request.GET.get('user')
#     username = request.GET.get('username')
#     address = request.GET.get('address')
#     context={
#     'username_data':username,
#     'address_data':address
#  }

#     return render(request, 'index.html', context)

def index(request):
    username = request.GET.get("username")    
    password = request.GET.get("password")
    print(username,password)
    context={
        'username_data':username,
        'password_data':password,
    }
    return render(request, 'base.html',context)

def summer(request,a,b):
    return  HttpResponse(f"the sum is {(a+b)}")

def home(request):
    username = request.GET.get("username")    
    password = request.GET.get("password")
    print(username,password)
    context={
        'username_data':username,
        'password_data':password,
    }
    return  render(request, 'home.html',context)

def mypage(request):
    context={
        
        'movie_list': ['animal' , 'leo','pushpa'],
        'favourite_movie': 'leo'
        
    }
    return render(request, 'mypage.html',context)


def multi(request):
    # username = request.GET('user')
    username = request.GET.get('user')
    address = request.GET.get('address')


    return HttpResponse(f"username is {username} and addrss is {address}")
 
def adminn(reqeust):
     return render (reqeust, 'admin.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",mypage),
    path("sum/<int:a>/<int:b>",summer),
    path("sum/<str:a>/<str:b>",summer),
    path('queryparams', multi),
    path('home',home),
    path("adminn/",adminn),
]
