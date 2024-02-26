from django.shortcuts import render
from blog.models import Post, Category, Tag, Menulist


def landing(request):
    recent_posts = Post.objects.order_by('-pk')[
                   :3]  # Post.object.order_by('-pk')는 Post의 pk의 역순으로 포스트를 가져와라 [:3]최근 3개만 가져와라
    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
            'menu_list_all': Menulist.objects.all(),
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'tags': Tag.objects.all(),
        }
    )



def site_introduction(request):
    return render(
        request,
        'single_pages/site_introduction.html',
        {
            'menu_list_all': Menulist.objects.all(),
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'tags': Tag.objects.all(),
        }
    )


# Create your views here.
