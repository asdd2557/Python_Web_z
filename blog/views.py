from email import message
from email.errors import StartBoundaryNotFoundDefect
from inspect import TPFLAGS_IS_ABSTRACT
from urllib import request, response
from xml.etree.ElementTree import Comment

from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .models import Post, Category, Tag, Comment, Menulist
from .forms import CommentForm

from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


##import tkinter //docker ckeditor_static_add


# -----------------------------menulist--------
##class MenuList(ListView):
##   model = Menulist

##   def get_context_data(self, **kwargs):
##       context = super(PostList, self).get_context_data()
##     context['menu_list_count'] = MenuList.objects.count()
##      context['menu_list_all'] = MenuList.objects.all()
##     return context


# -----------------------------menulist 끝--------

class PostList(ListView):

    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'
    paginate_by = 5  # 페이지당 몇개의 게시물을 표시할까?

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['menu_list_all'] = Menulist.objects.all()  ##Menu List
        context['tags'] = Tag.objects.all()
        return context


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):  ##UserPassesTestMixin를 거쳐서 통과될시에 나오는 메소드
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (
                current_user.is_staff or current_user.is_superuser):  ##로그인을 했고 로그인한 유저가 스테프유저인가 아님 슈퍼유전가
            form.instance.author = current_user
            response = super(PostCreate, self).form_valid(form)
            tags_str = self.request.POST.get('tags_str')
            if tags_str:

                tags_str = tags_str.strip()  ##문자열 앞뒤에 빈공간이 있으면 없에준다.
                tags_str = tags_str.replace(',', ';')  ## ,는 ;로 교체한다.
                tags_list = tags_str.split(';')  ## ;를 기준으로 리스트 를 생성하라
                for t in tags_list:
                    t = t.strip()  ## 앞뒤 빈공간 없에준다.
                    tag, is_tag_created = Tag.objects.get_or_create(name=t)  ##만약에 get을 하며 Tag중 T가있으면 가져오고 없으면 만들어서 가져와라라는 뜻임 이름이 T가있으면 tag함수에담고 두번째에 False를 반환함
                    if is_tag_created:
                        tag.slug = slugify(t, allow_unicode=True)
                        tag.save()
                    self.object.tags.add(tag)  ##새로 만든 게시물의 테그를 가져와 추가시킨다.

            return response

        else:
            return redirect('/blog/')

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data()
        context['menu_list_all'] = Menulist.objects.all()  ##Menu List
        return context


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
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'menu_list_all': Menulist.objects.all()  ##Menu List
        }
    )


def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
            'tags': Tag.objects.all(),
            'menu_list_all': Menulist.objects.all(),##Menu List
    }

    )


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        context['menu_list_all'] = Menulist.objects.all()  ##Menu List
        context['ckedit'] = Post.content
        context['tags'] = Tag.objects.all()
        return context


# Create your views here.

class PostUpdate(LoginRequiredMixin, UpdateView):  ##Updateview는 수정하려는 게시물의 레코드를 DB에서 불러와 아래 self.get_object()함수로 불러온다.
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    template_name = 'blog/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()


        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = ';'.join(tags_str_list)
        context['menu_list_all'] = Menulist.objects.all()  ##Menu List
        return context

    def form_valid(self, form):
        response = super(PostUpdate, self).form_valid(form)

        self.object.tags.clear()

        tags_str = self.request.POST.get('tags_str')
        if tags_str:
            tags_str = tags_str.strip()  ##문자열 앞뒤에 빈공간이 있으면 없에준다.
            tags_str = tags_str.replace(',', ';')  ## ,는 ;로 교체한다.
            tags_list = tags_str.split(';')  ## ;를 기준으로 리스트 를 생성하라
            for t in tags_list:
                t = t.strip()  ## 앞뒤 빈공간 없에준다.
                tag, is_tag_created = Tag.objects.get_or_create(name=t)  ##만약에 get을 하며 Tag중 T가있으면 가져오고 없으면 만들어서 가져와라라는 뜻임 이름이 T가있으면 tag함수에담고 두번째에 False를 반환함
                if is_tag_created:
                    tag.slug = slugify(t, allow_unicode=True)
                    tag.save()
                self.object.tags.add(tag)  ##새로 만든 게시물의 테그를 가져와 추가시킨다.

        return response

    def dispatch(self, request, *args, **kwargs):  ## 유저가 해당포스터를 수정할 권리가 있는지 검사 디스패치는 Get방식인지 Post방식인지 구분해주는 역활을 한다.
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied  ##장고에서 지원하는 기능으b 로 웹코드 200이 안뜨도록 하는 기능임


@csrf_exempt
# Create your views here.
def new_comment(request, pk):

        post = get_object_or_404(Post, pk=pk)  ## 포스트 키를 존재하지 않는 키로 요청할 경우 에러를 띄운다.

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.nickname = request.POST.get('nickname')
                comment.password = request.POST.get('password')
                comment.save()
                return redirect(comment.get_absolute_url())
        return redirect(post.get_absolute_url())




class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm



@csrf_exempt
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post

    if request.password == comment.password:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied  # 해커가 url로 delete_comment.pk를 이용하여 삭제할 수도 있기 때문에 방지하기 위하여 로그인한 사용자의 권한을 확인함


class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)  # 제목에  q가있거나 tags에 q가있을경우 표출해줌
        ).distinct()  # 만약 '파이썬'을 검색하면 파이썬이 포함되여있는 포스트가 나타나겠지만 만약 제목과 카테고리 둘다 파이썬이 포함되여있을경우 그 해당 포스트는 2번 노출되기 때문에 distinct()를 사용시 이를 해결할 수 있다.(중복 방지)
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'
        return context




def test_view(request):
    return render(request, 'blog/Test.html')