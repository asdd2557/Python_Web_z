from django.shortcuts import render
from blog.models import Post

def landing(request):
    recent_posts= Post.objects.order_by('-pk')[:3] #Post.object.order_by('-pk')는 Post의 pk의 역순으로 포스트를 가져와라
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )
# Create your views here.
