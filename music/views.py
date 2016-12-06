from django.http import HttpResponse
from .models import  Album
from django.template import loader



def index(request):
    all_Albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums' : all_Albums
    }
    return HttpResponse(template.render(context,request))

def detail(request,album_id):
    return HttpResponse("<h2>Details of "+str(album_id)+"</h2>")

