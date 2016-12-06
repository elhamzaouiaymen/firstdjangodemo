from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1> this is the music your are looking for ...</h1>")

def detail(request,album_id):
    return HttpResponse("<h2>Details of "+str(album_id)+"</h2>")

