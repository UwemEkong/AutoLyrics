from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Specific Song 
class Song(models.Model): 
    ARTIST_CHOICES = (
        ('Kanye_West', 'Kanye West'),
        ('Bruno_Mars', 'Bruno Mars'),
        ('The_Beatles', 'The Beatles'),
        ('Alicia_Keys', 'Alicia Keys'),
        ('Bob_Marley', 'Bob Marley'),
        ('Lil_Wayne', 'Lil Wayne'),
        ('Adele', 'Adele'),
        ('Justin_Bieber', 'Justin Bieber'),
        ('Britney_Spears', 'Britney Spears'),
        ('DJ_Khaled', 'DJ Khaled'),

    )
    # Every Created Song will be linked to a specific user
    artist = models.CharField(max_length = 50, choices=ARTIST_CHOICES, null=True)
    title = models.CharField(max_length=200)
    lyrics = models.TextField(null=True)
    uniqueUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this song."""
        return reverse('song-detail', args=[str(self.id)])

import uuid

#Song that the user saved
class UserSong(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a particular song')
    song = models.ForeignKey('Song', on_delete=models.SET_NULL, null =True)
    uniqueUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f'{self.id} ({self.song.title})'
