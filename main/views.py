from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Ridya Azizah Khayyira Mumtaz',
        'kelas' : 'PBP-A',
    }

    return render(request, "main.html", context)