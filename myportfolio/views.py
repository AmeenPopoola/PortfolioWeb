from django.shortcuts import render
from .models import Home,About,Profile,Category,Skills,Portfolio

def index(request):
    
    #HOME SECTION
    home = Home.objects.latest('updated')
    
    #ABOUT SECTION
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about = about)
    
    #SKILLS SECTION
    categories = Category.objects.all()
    
    #Portfolio
    portfolios = Portfolio.objects.all()
    
    
    context = {
        'home' : home,
        'about' : about,
        'profile' : profiles,
        'categories' : categories,
        'portfolios' : portfolios,
    }
    
    return render(request, 'index.html', context)

