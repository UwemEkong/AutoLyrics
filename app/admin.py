from django.contrib import admin

from .models import Song, UserSong

class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'lyrics')
admin.site.register(Song, SongAdmin)

class UserSongAdmin(admin.ModelAdmin):
    list_display = ('song', 'id', 'uniqueUser')
    fieldsets = (
        (None, {
            'fields': ('song','id','uniqueUser')
        }),
       
    )

admin.site.register(UserSong, UserSongAdmin)
