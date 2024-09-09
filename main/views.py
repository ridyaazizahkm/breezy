from django.shortcuts import render

def show_main(request):
    context = {
        'nama' : 'Ridya Azizah Khayyira Mumtaz',
        'kelas' : 'PBP-A',
        
        'name' : 'Alchemist Fragrance - Galleria | Eau de Parfum',
        'price': '229.000',
        'description': 'Alchemist Galleria perfume captures the essence of pure femininity, surrounding you with sweet florals that inspire romance and relaxation, making each moment beautifully serene.',
        'ukuran' : '50 ml',
        'aroma' : 'Sweet floral',
        'top_notes' : 'Cape jasmine, plum',
        'middle_notes' : 'Tuberose, oiellet',
        'base_notes' : 'Honey, redwood'
    }

    return render(request, "main.html", context)