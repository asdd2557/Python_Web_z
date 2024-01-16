from django.shortcuts import render
from blog.models import Post, Menulist

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3] #Post.object.order_by('-pk')는 Post의 pk의 역순으로 포스트를 가져와라 [:3]최근 3개만 가져와라
    menu_list_all = Menulist.objects.all()
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
            'menu_list_all': menu_list_all,
        }
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

def menutest(request):
    return render(
        request,
        'single_pages/menutest.html'
    )
# Create your views here.
