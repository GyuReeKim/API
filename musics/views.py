from django.shortcuts import render, get_object_or_404
from .models import Music, Artist, Comment
from rest_framework.decorators import api_view
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
from rest_framework.response import Response

# Create your views here.

# GET, POST, PUT/PATCH, DELETE
# Read, Create, Update, Delete
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

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, id):
    artist = get_object_or_404(Artist, id=id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # vaildation 과정에서 오류가 나면 405오류를 보내준다.
        serializer.save(music_id=id) # commit=False와 같은 역할을 한다.
    return Response(serializer.data)

# api/v1/comments/<int:id>/
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            # return Response({'message':"업데이트!!!"}) # 수정되면 메세지를 보여준다.
    else:
        comment.delete()
        return Response({'message':"삭제되었습니다!!!"})