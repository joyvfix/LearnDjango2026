from django.http import HttpResponse
from django.shortcuts import render

# method view
def trulala(request):
    context = {
        "judul":"Selamat Datang di Website Kelas",
        "nama":"Ahcuy",
        "kelas":"Web Development Django"
    }
    return render(request,'index.html',context)

# def index(request):
#     return HttpResponse('<h1>ini adalah Home</h1>')

# def about(request):
#     return render(request,'about.html')