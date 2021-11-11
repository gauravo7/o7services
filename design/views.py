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