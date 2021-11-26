from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.conf.urls.static import static
from . models import Staff,Category

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
def search3(request):
    obj = Staff.objects.get(pk=request.GET['id'])
    return render(request,"design/single.html",{"data":obj})
def searchform(request):
    obj = Staff.objects.all()
    return render(request,"design/dropdown.html",{"data":obj})
def update(request):
    if(request.method=="GET"):
        return redirect(search)
    else:
        obj = Staff.objects.get(pk=request.POST['id'])
        obj.name = request.POST['name']
        obj.password = request.POST['password']
        obj.save()
        return redirect(viewall)

def delete(request):
    obj = Staff.objects.get(pk=request.GET['id'])
    obj.delete()
    return redirect(viewall)
    
def delete2(request,id):
    # obj = Staff.objects.get(pk=request.GET['id'])
    # obj.delete()
    return HttpResponse("Hello"+str(id))
def data(request,id):
    print(request);
    return HttpResponse("Hie")
def urlji(request,id,cid):
    return HttpResponse("Hello")

def savecat(request,cname):
    obj = Category()
    obj.c_name = cname
    obj.save()
    return HttpResponse("Record Saved")