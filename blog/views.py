from email import message
from email.errors import StartBoundaryNotFoundDefect
from inspect import TPFLAGS_IS_ABSTRACT
from urllib import request, response
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView ,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Category, Tag
from .forms import CommentForm

from django.core.exceptions import PermissionDenied
import tkinter
import tkinter.messagebox
def test1(request):
     return render(request,'blog/Test.html' ) 


class PostList( ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostCreate(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self): ##UserPassesTestMixin를 거쳐서 통과될시에 나오는 메소드
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):##로그인을 했고 로그인한 유저가 스테프유저인가 아님 슈퍼유전가
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)
            tags_str = self.request.POST.get('tags_str')
            if tags_str:
    
                tags_str = tags_str.strip()##문자열 앞뒤에 빈공간이 있으면 없에준다.
                tags_str = tags_str.replace(',', ';')## ,는 ;로 교체한다.
                tags_list = tags_str.split(';') ## ;를 기준으로 리스트 를 생성하라                 
                for t in tags_list:
                    t = t.strip()## 앞뒤 빈공간 없에준다.
                    tag, is_tag_createed = Tag.objects.get_or_create(name=t) ##만약에 get을 하며 Tag중 T가있으면 가져오고 없으면 만들어서 가져와라라는 뜻임 이름이 T가있으면 tag함수에담고 두번째에 False를 반환함
                    if is_tag_createed:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag) ##새로 만든 게시물의 테그를 가져와 추가시킨다.

            return response
        else:
            return redirect('/blog/')


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all() 

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category = None).count(),
        }
    )



def category_page(request, slug):
    if  slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category = None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category = category)





    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }

    )



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form']= CommentForm
        return context
# Create your views here.

class PostUpdate(LoginRequiredMixin, UpdateView): ##Updateview는 수정하려는 게시물의 레코드를 DB에서 불러와 아래 self.get_object()함수로 불러온다.
    model = Post
    fields = ['title','hook_text','content','head_image','file_upload','category']

    template_name = 'blog/post_update_form.html' 

    def get_context_data(self, **kwargs): 
        context = super(PostUpdate, self).get_context_data()
     
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = ';'.join(tags_str_list)

        return context
        
    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)
      
        self.object.tags.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()##문자열 앞뒤에 빈공간이 있으면 없에준다.
            tags_str = tags_str.replace(',', ';')## ,는 ;로 교체한다.
            tags_list = tags_str.split(';') ## ;를 기준으로 리스트 를 생성하라                 
            for t in tags_list:
                t = t.strip()## 앞뒤 빈공간 없에준다.
                tag, is_tag_createed = Tag.objects.get_or_create(name=t) ##만약에 get을 하며 Tag중 T가있으면 가져오고 없으면 만들어서 가져와라라는 뜻임 이름이 T가있으면 tag함수에담고 두번째에 False를 반환함
                if is_tag_createed:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag) ##새로 만든 게시물의 테그를 가져와 추가시킨다.

        return response

    
            

    def dispatch(self, request, *args, **kwargs): ## 유저가 해당포스터를 수정할 권리가 있는지 검사 디스패치는 Get방식인지 Post방식인지 구분해주는 역활을 한다.
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied ##장고에서 지원하는 기능으로 웹코드 200이 안뜨도록 하는 기능임


def landing(request):
     return render(
        request,
        'blog/landing.html'
     )

def about_me(request):
     return render(
        request,
        'blog/about_me.html'
        )
# Create your views here.
def new_comment(request, pk):
    if request.user.is_authenticated: ##로그인했을경우
        post = get_object_or_404(Post, pk=pk) ## 포스트 키를 존재하지 않는 키로 요청할 경우 에러를 띄운다.

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        return redirect(post.get_absolute_url())
    else: 
        raise PermissionError  ## 로그인도 안됐는데 포스트형식으로 정보를 계속 보내면 에러매세지를 띄운다