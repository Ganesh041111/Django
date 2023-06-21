from django.http import HttpResponse
from django.shortcuts import render, redirect

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

def calculation(request):
    data={}
    try:
        if request.method == "POST":
            
            v1=int(request.POST.get("val1"))
            v2=int(request.POST.get("val2"))
            ans=v1+v2
            
            data={
                "val1":v1,
                "val2":v2,
                "output":ans
            }

            print(ans)
            return redirect("/")
    except:
        print("ans")
    return render(request, "calculation.html", data)
