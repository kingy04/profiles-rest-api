from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
