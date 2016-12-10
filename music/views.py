from django.http import HttpResponse
from .models import  Album
from django.http import Http404
from django.shortcuts import render



def index(request):
    all_Albums = Album.objects.all()
    context = {'all_albums' : all_Albums}
    return render(request,'music/index.html',context)

def detail(request,album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise  Http404("The album you are looking for does not exist anymore !")
    return render(request, 'music/detail.html', {'album': album})

