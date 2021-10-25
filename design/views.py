from django.shortcuts import render

from django.conf.urls.static import static

# Create your views here.

def index(request):
    return render(request,"design/index.html")
def about(request):
    return render(request,"design/about.html")
def contact(request):
    return render(request,"design/contact.html")