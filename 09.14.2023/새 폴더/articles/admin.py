from django.contrib import admin

from django.contrib import admin
from .models import Article
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','title','content',]
    list_display_links = ['title',]


admin.site.register(Article,AuthorAdmin)