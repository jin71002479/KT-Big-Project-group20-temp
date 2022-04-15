from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate, login, logout

def LoginView(request):
    return HTTPResponse(request, 'login.html')


def signup(request):
    if request.method == "POST": # 요청메시지가 post 라면
        print(request.POST)
        user_id = request.POST["user_id"]
        password = request.POST["password"]
        name = request.POST["name"]
        phone = request.POST["PhoneNumber"]
        age = request.POST["age"]
        gender = request.POST["gender"]
        parmacy = request.POST["parmacy"]
        
        if 'relation' in request.POST:
            relation = request.POST['relation']
        else:
            relation = False
        

        user = User.objects.create_user(name,password,user_id,phone,age,gender,parmacy)
        user.name = name
        user.password= password
        user.user_id = user_id
        user.phone = phone
        user.age = age
        user.gender = gender
        user.parmacy = parmacy 
        user.save()

        
        return redirect("member:login")

    return render(request, "signup.html")
