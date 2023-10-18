from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer,ArticleSerializer


@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        # django는 파이썬에게만 응답하지 않고 다양한 언어의 클라이언트에게 응답 -->   유연한 데이터타입으로 바꿔야
        # articles 데이터가 쿼리셋처럼 다중데이터라면 many= True로 해줘야(default는 False)
        serializer = ArticleListSerializer(articles,many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data = request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            

@api_view(['GET','DELETE','PUT'])
def article_detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "GET":
    # 단일인 스턴스 하나이고 쿼리셋 아니므로 many 설정 안해줌
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "DELETE":
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)