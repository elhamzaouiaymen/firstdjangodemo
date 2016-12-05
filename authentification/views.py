from django.http import HttpResponse

def authentification(request):
    return HttpResponse("<h2>You have to login dear user !</h2>")

