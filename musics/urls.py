from django.urls import path
from . import views

app_name = "musics"

urlpatterns = [
    path('musics/', views.music_list, name="music_list"), # api 서버에서는 name이 사실상 필요하지 않다.
    path('musics/<int:id>/', views.music_detail, name="music_detail",)
]
