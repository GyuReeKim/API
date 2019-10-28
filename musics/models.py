from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.TextField()

class Comment(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    content = models.TextField()
