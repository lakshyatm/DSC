from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('second/',views.second,name="second"),
    path('second/third/',views.third,name="third"),
    path('second/third/final/',views.fourth,name="fourth"),
]
