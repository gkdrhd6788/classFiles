from django.urls import path
from . import views
# app_name = 'articles'
urlpatterns = [
    path('throw/', views.throw, name = 'throw'),
    path('catch/',views.catch),
    path('introduce/<str:name>/<int:age>/',views.introduce, name = 'introduce'),
    ]