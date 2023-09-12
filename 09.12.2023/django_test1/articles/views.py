from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    context = {
        'name':'sooji',
        'age':29,
    }
    return render(request,'articles/index.html',context)