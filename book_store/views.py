from django.http import HttpResponse

def index(request):
    return HttpResponse("welcome to my book store.")

# Create your views here.
