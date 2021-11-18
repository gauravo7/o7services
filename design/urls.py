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


]
