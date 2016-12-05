from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1> this is the music your are looking for ...</h1>")