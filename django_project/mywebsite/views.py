from django.http import HttpResponse
from django.shortcuts import render

# method view
def trulala(request):
    return render(request,'index.html')

def index(request):
    return HttpResponse('<h1>ini adalah Home</h1>')

def about(request):
    return render(request,'about.html')