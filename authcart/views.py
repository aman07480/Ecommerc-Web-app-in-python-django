from django.shortcuts import render,redirect

# Create your views here.
def signup(request):
    return render (request,'authintication/signup.html')


def login(request):
    return render (request,'authintication/login.html')


def logout(request):
    return redirect (request,'/authcart/login')
