from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.parsers import JSONParser
from . models import Song, Artist, UserSong
from . serializers import SongSerializer
from . forms import SongForm
import pickle
import markovify
import json
import os

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

#Replace unnecessary characters in order to read correct pickle file
def cleanString(fileName):
    new_name = str(fileName.replace(" ", "_"))
    return new_name

 

#Utilize pre-trained model in order to generate text
def generateText(artistID):

    new_ID = cleanString(artistID)

    with open('app/' + new_ID + '.pickle', 'rb') as f:
        model = pickle.load(f)
    newLyrics = ""
    for i in range(20):
        newLyrics += ' ' + model.make_sentence(tries=25)
    return newLyrics

#Handle POST request by returning generated song lyrics
def markovifyText(unit):
    try:
        lyrics = generateText(unit["Artist"])
        return lyrics
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

#Present the user with a unique song based on the chosen artist
def userContact(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            Title = form.cleaned_data['Title']
            Artist = form.cleaned_data['Artist']
            myDict = (request.POST).dict()
            answer = markovifyText(myDict)
            messages.success(request,  myDict['Title'] + ':' + answer)
        return redirect('customsong')

    form = SongForm()

   
    return render(request, 'myform/index.html', {'form': form})

#Song page that the user gets redirected to
def customsong(request):
    return render(request, 'myform/customsong.html')
