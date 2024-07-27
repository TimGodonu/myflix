from django.shortcuts import render,HttpResponse 

# Create your views here.
def index(request):
    return render(request, 'movies/index.html',{})

def aboutus(request):
    return render(request, 'movies/aboutus.html',{})