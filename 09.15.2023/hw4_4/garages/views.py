from django.shortcuts import render
from .models import Garage
# Create your views here.
def garage(request):
    garages = Garage.objects.all()
    dokdo = Garage.objects.filter(location='독도')
    capa = Garage.objects.filter(capacity__lte=30)
    ava = Garage.objects.filter(is_parking_available=True)
    context = {
        'garages':garages ,
        'dokdos':dokdo,
        'capas':capa,
        'avas':ava,
    }
    return render(request,'garages/index.html',context)