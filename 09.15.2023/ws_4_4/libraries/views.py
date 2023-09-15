from django.shortcuts import render
from .models import Book
# Create your views here.
def title(request):
    books = Book.objects.all()
    context = {
        'books' : books,
                }
    return render(request,'libraries/index.html',context)