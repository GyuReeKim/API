from django.urls import path
from . import views

app_name = "musics"

urlpatterns = [
    path('musics/', views.music_list, name="music_list"), # api 서버에서는 name이 사실상 필요하지 않다.
    path('musics/<int:id>/', views.music_detail, name="music_detail",),
    path('artists/', views.artist_list, name="artist_list"),
    path('artists/<int:id>/', views.artist_detail, name="artist_detail",),
    path('musics/<int:id>/comments/', views.comment_create),
    path('comments/<int:id>/', views.comment_detail),
]
