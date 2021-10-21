from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('page1',views.page1,name="page1"),
    path('page2',views.page2,name="page2"),
    path('page3',views.page3,name="page3"),
    path('page4',views.page4,name="page4"),
    path('form',views.form,name="form"),
    path('formhadler',views.formhadler,name="formhadler"),
    path('formnumber',views.formnumber,name="formnumber"),
    path('submitnum',views.submitnum,name="submitnum"),
    path('passvalueinview',views.passvalueinview,name="passvalueinview"),
    path('passarray',views.passarray,name="passarray"),
    path('passmultiple',views.passmultiple,name="passmultiple"),
    path('passmultiple2',views.passmultiple2,name="passmultiple2"),

    path("first",views.first,name="first"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),

]
