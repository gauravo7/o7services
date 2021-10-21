from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome<br/></h1>")

def page1(request):
    return render(request,"students/page1.html")

def page2(request):
    return render(request,"students/page2.html")

def page3(request):
    return render(request,"students/page3.html")

def page4(request):
    return render(request,"page4.html")
def form(request):
    return render(request,"students/form.html")

def formhadler(request):
    name = request.POST['name']
    pass1 = request.POST['pass']
    return HttpResponse("In Form handler"+name+pass1)

def formnumber(request):
    return render(request,"students/Numbers.html")
def submitnum(request):
    x=  int(request.GET['one'])
    y=  int(request.GET['two'])
    temp=""
    for i in range(x+y):
        temp += "<br/>"+str(i)
    return HttpResponse((temp))

def passvalueinview(request):
    data = 100
    return render(request,"students/passvalueinview.html",{"myvar":1100})


def passarray(request):
    data = [1,2,3,4,5,6,7]
    return render(request,"students/passarray.html",{"myvar":data})

def passmultiple(request):
    a = 100
    b = 200
    c = 300
    return render(request,"students/passmultiple.html",{"A":a,"B":b,"C":c})
def passmultiple2(request):
    data = {
        "a":100,
        "b":200,
        "c":300
    }
    return render(request,"students/passmultiple1.html",{"data":data})

def first(request):
    return render(request,"students/first.html")
    
def about(request):
    return render(request,"students/about.html")
    
def contact(request):
    return render(request,"students/contact.html")
