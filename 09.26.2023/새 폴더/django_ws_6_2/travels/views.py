from django.shortcuts import render,redirect
from .forms import TravelsForm
from .models import Travels
# Create your views here.
def index(request):
    travels= Travels.objects.all 
    context = {
        'travels': travels, 
    }
    return render(request,'travels/index.html',context)


def new(request):
    form = TravelsForm()
    context={
        'form':form,
    }
    return render(request,'travels/create.html',context)

def create(request):
    form = TravelsForm(request.POST)
    if form.is_valid():
        print('------------------------------------------------')
        
        a = form.save()
        print(a.pk)
        return redirect('travels:index')
    context = {
        'form':form,
    }
    return render(request,'travels/create.html',context)
    