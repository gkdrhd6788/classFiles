from django.urls import path
from . import views

urlpatterns = [
    path('calculator/<int:first_num>/<int:second_num>',views.cal)
]
