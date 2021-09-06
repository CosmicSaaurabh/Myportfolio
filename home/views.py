from django.shortcuts import render, HttpResponse
from home import models 


# Create your views here.

def index(request):
    #  return HttpResponse("u are very welcome here!, You can now start django hoep you will enjoy")
    # to pass any varible to html page we can use dictionary to work
    context = {'name' : 'Saurabh' , 'Profession': 'Student'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project.html')

def contactme(request):
    if request.method == "POST":
        print("This is post method")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['message']
        ins = models.Contact(name = name, email = email, phone = phone, desc = desc)
        ins.save()
        print("the data has been written to db")

    return render(request, 'contactme.html')

def Achievements(request):
    return render(request, 'Achievements.html')

def Links(request):
    return render(request, 'Links.html')

 