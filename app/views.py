from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def nandu(request):
    return HttpResponse('<marquee><h1>Nandu is my fav name</h1></marquee>')

def aishu(request):
    return HttpResponse('<h1>Aishu is good girl</h1>')