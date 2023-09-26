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

def detail(request,travel_pk):
    travel = Travels.objects.get(pk=travel_pk)
    context ={
        'travel': travel,
    }
    return render(request,'travels/detail.html',context)

# def new(request):
#     form = TravelsForm()
#     context={
#         'form':form,
#     }
#     return render(request,'travels/create.html',context)

def create(request):
    if request.method=="POST":
        form = TravelsForm(request.POST)
        if form.is_valid():
            a=form.save()
            # print(a)
            return redirect('travels:detail',a.pk)
        
    else:
        form = TravelsForm()
    context={
        'form':form,
    }
    return render(request,'travels/create.html',context)