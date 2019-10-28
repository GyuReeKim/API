from rest_framework import serializers
from .models import Music

# json처럼 직렬화 하는 것을 serialization이 해준다.
class MusicSerializer(serializers.ModelSerializer): # 모델을 가져와 처리를 해 줄 새로운 class 생성
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id',)