from django.shortcuts import render, HttpResponse



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
    return render(request, 'contactme.html')

 