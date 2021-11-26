from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('form',views.form,name="form"),
    path('formsubmit',views.formsubmit,name="formsubmit"),
    path('viewall',views.viewall,name="viewall"),
    path('dbselector',views.dbselector,name="dbselector"),
    path('search',views.search,name="search"),
    path('search2',views.search2,name="search2"),
    path('update',views.update,name="update"),
    path('delete',views.delete,name="delete"),
    path('searchform',views.searchform,name="searchform"),
    path('search3',views.search3,name="search3"),
    path('delete2/<int:id>',views.delete2,name="delete2"),
    path('urlji/<int:id>/<int:cid>',views.urlji,name="urlji"),
    path('savecat/<str:cname>',views.savecat,name="savecat"),

]
