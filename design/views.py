from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.conf.urls.static import static
from . models import Staff

# Create your views here.

def index(request):
    return render(request,"design/index.html")
def about(request):
    return render(request,"design/about.html")
def contact(request):
    return render(request,"design/contact.html")
def form(request):
    return render(request,"design/form.html")
def formsubmit(request):
    obj = Staff()
    obj.name = request.POST['name']
    obj.email = request.POST['email'] 
    obj.password = request.POST['password']
    obj.save()
    return redirect("form")
def viewall(request):
    a = Staff.objects.all()
    return render(request,"design/viewall.html",{"data":a})

# def dbselector(request):
#     a = Staff.objects.get(pk=2)
#     print(a.name)
#     return HttpResponse(a.name)
def dbselector(request):
    a = Staff.objects.filter(password='123')
    temp=""
    for i in a:
        temp += i.name+"<br/>"
    return HttpResponse(temp)

def search(request):
    if(request.method=="GET"):
        return render(request,"design/search.html")
    else:
        obj = Staff.objects.get(pk=request.POST['id'])
        return render(request,"design/single.html",{"data":obj})
def search2(request):
    obj = Staff.objects.get(pk=request.GET['id'])
    return render(request,"design/single.html",{"data":obj})
def update(request):
    if(request.method=="GET"):
        return redirect(search)
    else:
        obj = Staff.objects.get(pk=request.POST['id'])
        obj.name = request.POST['name']
        obj.password = request.POST['password']
        obj.save()
        return redirect(viewall)