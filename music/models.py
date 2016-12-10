from django.db import models

class Album(models.Model): #Album herits from the class Model
    artist = models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre = models.CharField(max_length=200)
    album_logo=models.CharField(max_length=1000) #it will contains the link of the logo image

    def __str__(self): #to string en java
        return self.album_title +'-'+ self.artist

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE) #cascade means when you delete the parent model, this child model with be deleted too
    file_type = models.CharField(max_length=5)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title



