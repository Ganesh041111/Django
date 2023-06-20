from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        "title":"My Home Page",
        "clist":["java", "python", "c++"],
        "numlist":[10, 20, 30, 40, 50]
    }
    return render(request, "index.html",data)

def aboutUs(request):
    return HttpResponse("<b> Hare Krishna | Shree Ganesh | Shree Swami Samartha | Jai Jagannatha </b>")

def courses(request):
    return HttpResponse("Hello World!!")

def course(request, courseid):
    return HttpResponse(courseid)
