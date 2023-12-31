from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer,ArticleSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializers = ArticleSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status =status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def article_detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "GET":
        serializers = ArticleSerializer(article)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        article.delete()
        return Response({'delete':f'게시글 {article_pk}번이 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)    
    elif request.method =="PUT":
        serializers = ArticleSerializer(article,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status = status.HTTP_201_CREATED)
        return Response(serializers.error,status = status.HTTP_400_BAD_REQUEST)
