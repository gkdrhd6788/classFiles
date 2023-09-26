from django.urls import path
from . import views
app_name="travels"
urlpatterns = [
    path('',views.index,name='index'),
    # path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    path('detail/<int:travel_pk>/',views.detail, name='detail'),
]