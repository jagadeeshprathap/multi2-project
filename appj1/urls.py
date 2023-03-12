from appj1.views import *
from django.urls import path
app_name="something"
urlpatterns=[
    path("sky/",sky,name="sky"),
]