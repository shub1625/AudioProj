from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer,PodcastSerializer,AudioBookSerializer
from .models import Song,Podcast,AudioBook



@api_view(['GET'])
def home_View(request):
    api_urls = {
        'List': '/audioFileType/',
        'Detail View': '/audioFileType/audioFildId',
        'Create' : '/create/',
        'Update' : '/update/audioFileType>/audioFildId/',
        'Delete' : '/delete/audioFileType>/audioFildId/'
    }

    return Response(api_urls)

@api_view(['GET'])
def audioList(request,audioFileType,pk=None):
    
    if audioFileType == 'songs':
        if pk is None:
            songs = Song.objects.all()
            serilaizer = SongSerializer(songs,many=True)
        else:
            song = get_object_or_404(Song,pk=pk)
            serilaizer = SongSerializer(song,many=False)
        return Response(serilaizer.data)
    elif audioFileType == 'podcasts':
        if pk is None:
            podcasts = Podcast.objects.all()
            serilaizer = PodcastSerializer(songs,many=True)
        else:
            podcast = get_object_or_404(Podcast,pk=pk)
            serilaizer = PodcastSerializer(podcast,many=False)
        return Response(serilaizer.data)
    elif audioFileType == 'audiobooks':
        if pk is None:
            audiobooks = AudioBook.objects.all()
            serilaizer = AudioBookSerializer(audiobooks,many=True)
        else:
            audiobook = get_object_or_404(AudioBook,pk=pk)
            serilaizer = AudioBookSerializer(audiobook,many=False)
        return Response(serilaizer.data)
    else:
        content = {'Invalid' : 'Please see api home for endpoints'}
        return Response(content,status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def audioCreate(request):
    
    audio_type = request.data['audioFileType']
    metadata = request.data['audioFileMetadata']

    if audio_type == 'song':
        serilaizer = SongSerializer(data=metadata)
    elif audio_type == 'podcast':
        serilaizer = PodcastSerializer(data=metadata)
    elif audio_type == 'audiobook':
        serilaizer = AudioBookSerializer(data=metadata)
    else:
        content = {'Invalid' : 'Invalid Data'}
        return Response(contet,status=status.HTTP_400_BAD_REQUEST)
    
    if serilaizer.is_valid():
        serilaizer.save()
        return Response(serilaizer.data)
    else:
        return Response(serilaizer.errors)


@api_view(['POST'])
def audioUpdate(request,audioFileType,pk):
    
    audio_type = request.data['audioFileType']
    metadata = request.data['audioFileMetadata']

    if audio_type == 'song':
        song = get_object_or_404(Song,pk=pk)
        serilaizer = SongSerializer(data=metadata,instance=song)
    elif audio_type == 'podcast':
        podcast =  get_object_or_404(Podcast,pk=pk)
        serilaizer = PodcastSerializer(data=metadata,instance=podcast)
    elif audio_type == 'audiobook':
        audiobook = get_object_or_404(AudioBook,pk=pk)
        serilaizer = AudioBookSerializer(data=metadata,instance=audiobook)
    else:
        content = {'Invalid' : 'Invalid Data'}
        return Response(contet,status=status.HTTP_400_BAD_REQUEST)
    
    if serilaizer.is_valid():
        serilaizer.save()
        return Response(serilaizer.data)
    else:
        return Response(serilaizer.errors)

@api_view(['DELETE'])
def audioDelete(request,audioFileType,pk):
    
    if audioFileType == 'songs':
        song = get_object_or_404(Song,pk=pk)
        song.delete()
    elif audioFileType == 'podcasts':
        podcast =  get_object_or_404(Podcast,pk=pk)
        podcast.delete()
    elif audioFileType == 'audiobooks':
        audiobook = get_object_or_404(AudioBook,pk=pk)
        audiobook.delete()
    else:
        content = {'Invalid' : 'Invalid Data'}
        return Response(content,status=status.HTTP_400_BAD_REQUEST)
    return Response("Item Succefully deleted",status=status.HTTP_200_OK)