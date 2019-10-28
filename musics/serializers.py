from rest_framework import serializers
from .models import Music, Artist, Comment

# json처럼 직렬화 하는 것을 serialization이 해준다.
class MusicSerializer(serializers.ModelSerializer): # 모델을 가져와 처리를 해 줄 새로운 class 생성
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id')

class ArtistSerializer(serializers.ModelSerializer): # 전체 리스트를 보여줄 때 사용
    class Meta:
        model = Artist
        fields = ('id', 'name')

class ArtistDetailSerializer(serializers.ModelSerializer): # detail 페이지를 보여줄 때
    # music_set = MusicSerializer(many=True)
    # class Meta:
    #     model = Artist
    #     fields = ('id', 'name', 'music_set')
    # music_set이름을 바꾸고 싶을 때 source 사용
    musics = MusicSerializer(source="music_set", many=True) # ArtistSerializer과 다르게 Artist의 모든 Music에 대한 정보를 볼 수 있다.
    musics_count = serializers.IntegerField(source="music_set.count") # source에는 music_set을 사용해야한다.
    class Meta:
        model = Artist
        fields = ('id', 'name', 'musics', 'musics_count')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id')