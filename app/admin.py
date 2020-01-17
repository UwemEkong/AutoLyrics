from django.contrib import admin

from .models import Song, UserSong, Artist

admin.site.register(Song)
admin.site.register(UserSong)
admin.site.register(Artist)