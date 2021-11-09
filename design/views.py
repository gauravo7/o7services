from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.conf.urls.static import static
from . import models

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
    obj = models.Staff()
    obj.name = request.POST['name']
    obj.email = request.POST['email'] 
    obj.password = request.POST['password']
    obj.save()
    return redirect("form")