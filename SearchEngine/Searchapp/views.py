from .forms import SignupForm
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import login

# Create your views here.

def homepage(request):
    return render(request,'home.html')


def loginForm(request):
    if request.method =="POST":
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')

            user=authenticate(username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    else:
        form=AuthenticationForm()

    return render(request,'login.html',{'form':form})


def logoutuser(request):
    logout(request)

    return redirect('home')



def Registration(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=SignupForm
    return render(request,'register.html',{'form':form})


import requests
from bs4 import BeautifulSoup as bs
import lxml


def Search(request):
    if request.method=='POST':
        srarch=request.POST['search']
        url='https://www.ask.com/web?q=' + search

        result= requests.get(url)
        s=bs(result.text,'lxml')

        result_list=s.find_all('div',{'class':'PartialSearchResult-item'})

        find_list = []
        for i in result_list:
            result_title= i.find(class_='PartialSearchResult-item-title')
            result_url=i.find('a').get('href')
            result_details = i.find(class_='PartialSearchResult-item-details')

        find_list.append(( result_title,result_url,result_details))
        
        context={
            'find_list': find_list
        }

        return render(request,'home.html',context)

    else:
        return render(request,'home.html')