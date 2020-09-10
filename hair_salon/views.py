from django.shortcuts import render, redirect, reverse
from .models import Cutting, Styling, Colour, Highlights, Toners, Treatment, Extension

# Create your views here.
def home(request):
    cutting = Cutting.objects.all().order_by('name')
    styling = Styling.objects.all().order_by('name')
    colour = Colour.objects.all().order_by('name')
    highlights = Highlights.objects.all().order_by('name')
    toners = Toners.objects.all().order_by('name')
    treatment = Treatment.objects.all().order_by('name')
    extension = Extension.objects.all().order_by('name')
    # return redirect(reverse('home'),
    return render(request, 'index.html',
        {'cutting': cutting, 'styling': styling, 
            'colour': colour, 'highlights': highlights,
            'toners': toners, 'treatment': treatment, 'extension':extension
        })
    
    

# About view
# def about(request):
#     return render(request, 'about.html')


# Gallery view
# def gallery(request):
#     return render(request, 'gallery.html')


# Services view
# def services(request):
#     cutting = Cutting.objects.all().order_by('name')
#     styling = Styling.objects.all().order_by('name')
#     colour = Colour.objects.all().order_by('name')
#     highlights = Highlights.objects.all().order_by('name')
#     toners = Toners.objects.all().order_by('name')
#     treatment = Treatment.objects.all().order_by('name')
#     extension = Extension.objects.all().order_by('name')
#     # return redirect(reverse('home'),
#     return render(request, 'index.html',
#         {'cutting': cutting, 'styling': styling, 
#             'colour': colour, 'highlights': highlights,
#             'toners': toners, 'treatment': treatment, 'extension':extension
#         })