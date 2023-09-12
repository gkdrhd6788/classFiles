from django.shortcuts import render

# Create your views here.
def hello(response):
    return render(response,'my_app/index.html')