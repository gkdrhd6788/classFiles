from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

def detail(request,pk):
    article= Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request,'articles/detail.html',context)


def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form=ArticleForm()
    context = {
        'form':form,
        }
    return render(request,'articles/create.html',context)

@require_POST
def delete(request,pk):
    article= Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request,pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        article = Article.objects.get(pk=pk)
        form=ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article,
        }
    return render(request,'articles/update.html',context)
