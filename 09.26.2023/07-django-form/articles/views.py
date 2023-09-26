from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html',context)


def create(request):
    # 요청의 메서드가 POST라면(creat와 new 합치기)
    if request.method == 'POST': #POST 기준으로 쓴 이유: GET/POST말고 나중에 2가지 더 있음
        form = ArticleForm(request.POST)
        # 유효성 검사
        # 유효성 검사가 통과된 경우
        if form.is_valid():  
            article = form.save()  #form.save()만 해도 되지만, 밑에서pk쓰기 위해 article로 받음
            return redirect('articles:detail',article.pk)
        
        # 에러메세지는 form으로 넘어감
        # context = {
        #     'form':form, 
        # }
        # # redirect(유지되지 못함. 에러메시지도 없음)가 아닌 render
        # return render(request,'articles/new.html',context)
        
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # return redirect('articles:index')
    else: # 요청의 메서드가 POST가 아니라면(new)
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)  #이렇게 넣어줘야 edit화면에서 기존 내용이 나옴
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 요청 메서드가 POST라면 (update)
    if request.method == 'POST':
        # article = Article.objects.get(pk=pk) # 공통이니까 위로 뺌
        # create와 비슷
        form = ArticleForm(request.POST,instance = article)  #인스턴스 안넣으면 create처럼 새로운 데이터가 생성됨-->인스턴스 유무로 저장인지 수정인지 판단
        if form.is_valid():  
            form.save()  #위에 article있기에 create와 달리 article로 안받음
            return redirect('articles:detail',article.pk)
        # context = {
        #     'form':form, 
        # }
        # return render(request,'articles/edit.html',context)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)
    # 요청 메서드가 POST가 아니라면 (edit)
    else:
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)  
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
