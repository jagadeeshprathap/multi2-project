from appj2.views import *
from django.urls import path
app_name="nothing"
urlpatterns=[
    path("chitti/",chitti,name="chitti"),
]