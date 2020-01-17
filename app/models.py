from django.db import models
from django.urls import reverse

# Specific Song 
class Song(models.Model): 
    ARTIST_CHOICES = (
        ('Kanye_West', 'Kanye_West'),
        ('Bruno_Mars', 'Bruno_Mars'),
        ('The_Beatles', 'The_Beatles'),
        ('Alicia_Keys', 'Alicia_Keys'),
        ('Bob_Marley', 'Bob_Marley'),
        ('Lil_Wayne', 'Lil_Wayne'),
        ('Adele', 'Adele'),
        ('Justin_Bieber', 'Justin_Bieber'),
        ('Britney_Spears', 'Britney_Spears'),
        ('DJ_Khaled', 'DJ_Khaled')

    )

    title = models.CharField(max_length=200)
    lyrics = models.TextField(null=True)

    def __str__(self):
        return self.title

import uuid

#Song that the user saved
class UserSong(models.Model):
    song = models.ForeignKey('Song', on_delete=models.SET_NULL, null =True)
    id = models.UUIDField(primary_key=True)
    

    def __str__(self):
        return f'{self.id} ({self.song.title})'


#Artist that the generated song is based on
class Artist(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name