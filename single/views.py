from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single/about_me.html'
    )
# Create your views here.