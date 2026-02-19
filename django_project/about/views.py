from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        "nama_kelas":"django beginner",
        "jumlah_siswa":"20",
        "aktif":"True"
    }
    return render(request,'about/about.html',context)