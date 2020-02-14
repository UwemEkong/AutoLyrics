from django.urls import path, include
from . import views


#Generates urls for a particular model
from rest_framework import routers

router = routers.DefaultRouter()
router.register('app', views.SongView)

urlpatterns = [
    path('songs/', views.SongListView.as_view(), name='songs'),
    path('home/', views.userContact, name ='index'),
    path('api/', include(router.urls)),
    path('lyrics/', views.markovifyText),
    path('newSong/,', views.customsong, name='customsong'),
    path('song/<int:pk>', views.SongDetailView.as_view(), name='song-detail'),
]

urlpatterns += [   
    path('mysongs/', views.UserSongListView.as_view(), name='my-songs'),
]


