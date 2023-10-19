from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Music,Comment
from .serializers import MusicListSerializer, MusicSerializer,CommentSerializer


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    if request.method == 'GET':
        serializers = MusicSerializer(music)
        return Response(serializers.data)
    
    elif request.method == 'DELETE':
        music.delete()
        data = {
            'delete': f'데이터 {music_pk}번 음악이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializers = MusicSerializer(music, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
        

@api_view(['GET',])
def comment_list(request):
    comments = Comment.objects.all()
    serializers = CommentSerializer(comments,many=True)
    return Response(serializers.data,status=status.HTTP_200_OK)


@api_view(['GET','DELETE','PUT'])
def comment_detail(request,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "GET":
        serializers = CommentSerializer(comment)
        return Response(serializers.data,status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        comment.delete()
        return Response({'delete':f'댓글 {comment_pk}번이 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serializers = CommentSerializer(comment,data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)

@api_view(['POST',])
def comment_create(request,music_pk):
    music = Music.objects.get(pk=music_pk)
    serializers = CommentSerializer(data= request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(music=music)
        return Response(serializers.data,status=status.HTTP_200_OK)
    