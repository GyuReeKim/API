from django.shortcuts import render, get_object_or_404
from .models import Music
from rest_framework.decorators import api_view
from .serializers import MusicSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all() # musics를 json 형태로 바꿔줘야 한다. (musics는 query 형태)
    serializer = MusicSerializer(musics, many=True) # 직렬화 작업을 해준다. 'many=True'는 데이터가 여러개일 때 사용한다.
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, id):
    music = get_object_or_404(Music, id=id)
    serializer = MusicSerializer(music)
    return Response(serializer.data)