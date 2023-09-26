from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles=Article.objects.all()
    context={
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

def detail(request,article_pk):
    article=Article.objects.get(pk=article_pk)
    context={
        'article': article,
    }
    return render(request,'articles/detail.html',context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form,
#     }
#     return render(request,'articles/new.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:index")
            # title=request.POST.get('title')
            # content = request.POST.get('content')
            # article=Article(title=title,content=content)
            # article.save()
        # context = {
        #     'form':form,
        # }
        # return render(request,'articles/new.html',context)
    # return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request,'articles/new.html',context)