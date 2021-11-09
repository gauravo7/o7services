from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('form',views.form,name="form"),
    path('formsubmit',views.formsubmit,name="formsubmit"),


]
