from .models import Music
from .serializers import MusicListSerializer,MusicSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializers = MusicListSerializer(musics,many=True)
        return Response(serializers.data,status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializers = MusicSerializer(data = request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status = status.HTTP_201_CREATED)
        

@api_view(['GET','DELETE','PUT'])     
def music_detail(request,music_pk):
    music = Music.objects.get(pk=music_pk)
    if request.method == 'GET':
        serializers = MusicSerializer(music)
        return Response(serializers.data,status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        music.delete()  #
        return Response({'delete':f'데이터 {music_pk}번 음악이 삭제되었습니다.'},status=status.HTTP_204_NO_CONTENT) 
    elif request.method == "PUT":
        serializers = MusicSerializer(music,data=request.data,partial=True) 
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status = status.HTTP_201_CREATED)

