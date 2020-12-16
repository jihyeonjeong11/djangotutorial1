from django.shortcuts import render, redirect
from NewsApp.models import News
from .forms import RegistrationForm, RegistrationModal
from .models import RegistrationData


# Create your views here.

def Home(request) :

    context= {
        "name": "jihyeonjeong"
    }

    return render(request, "home.html", context)
    
def Newspage(request) : 
    obj = News.objects.get(id=1)

    context = {
        "data": obj
    }

    return render(request, "news.html", context)
    
def contact(request) : 
    return render(request, "contact.html")
    
def NewsDate(request, year) :

    article_list = News.objects.filter(pub_date__year = year)

    context = {
        'year':year,
        'article_list': article_list
    }

    return render(request, 'newsdate.html', context)

def Register(request) : 

    context = {
        "form": RegistrationForm

    }

    return render(request, "register.html", context)

def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password'],
                                    email = form.cleaned_data['email'],
                                    phone = form.cleaned_data['phone'],
                                                                             )
        myregister.save()

    return redirect('Home')

def modelform(request):

    context = {
        'modalform': RegistrationModal
    }

    return render(request, 'modalform.html', context)

def addModalForm(request):
    mymodalform = RegistrationModal(request.POST)

    if mymodalform.is_valid():
        mymodalform.save()

    return redirect('Home')