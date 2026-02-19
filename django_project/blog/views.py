from django.shortcuts import render

# Create your views here.
def blog2(request):
    context ={
          "judul_blog": "Daftar Artikel",
        "artikel": [
            "Belajar Django Dasar",
            "Memahami URL dan Views",
            "Belajar Template Django",
        ]
    }
    return render (request,'blog/blog.html',context)