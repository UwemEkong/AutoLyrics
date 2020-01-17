from django.urls import path, include
from . import views
from rest_framework import routers

#Generates urls for a particular model
from rest_framework import routers

router = routers.DefaultRouter()
router.register('app', views.SongView)

urlpatterns = [
    path('home/', views.userContact, name ='index'),
    path('api/', include(router.urls)),
    path('lyrics/', views.markovifyText),
    path('song/,', views.customsong, name='customsong'),
]

