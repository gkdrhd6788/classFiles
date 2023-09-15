from django.contrib import admin
from .models import Book
# Register your models here.

class  AuthorAdmin(admin.ModelAdmin):
    list_display = ['author','title','price','pubdate']
admin.site.register(Book,AuthorAdmin)
