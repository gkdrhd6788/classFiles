from django.shortcuts import render,redirect
from .forms import TravelsForm
from .models import Travels
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET"])
def index(request):
    travels= Travels.objects.all 
    context = {
        'travels': travels, 
    }
    return render(request,'travels/index.html',context)

@require_http_methods(["GET"])
def detail(request,travel_pk):
    travel = get_object_or_404(Travels, pk=travel_pk)
    # travel = Travels.objects.get(pk=travel_pk)
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
@require_http_methods(["GET","POST"])
def create(r equest):
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