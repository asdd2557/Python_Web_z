from django.db import models
from django.contrib.auth.models import User
import os
from markdown import markdown
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True,allow_unicode=True) #SlugField는 기본적으로 한글을 지원하지 않아서 allow_unicode = True는 한국어를 사용할 수 있게해주는 언어다.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories' #해당 목록글씨를 'Categories'로 바꿔준다.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True,allow_unicode=True) #SlugField는 기본적으로 한글을 지원하지 않아서 allow_unicode = True는 한국어를 사용할 수 있게해주는 언어다.

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'



class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()# models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #미디어 파일 안에 블로그 안에 이미지 안에 년도 월 로 만듬
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)#blank 는 공백이라는 뜻이므로 blank = True는 공백을 허가하겠다는 뜻이다. null은 추후에 value가 삭제될시에 null로 변환을 허용한다는 뜻

    tags = models.ManyToManyField(Tag, blank=True)




    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    def get_content_markdown(self):  ##컨텐트를 마크다운형식으로 바꿔준다. 
        return markdown(self.content)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) ##해당 글이 삭제될경우 연관된 댓글도 같이 삭제됨
    author = models.ForeignKey(User, on_delete=models.CASCADE) ##유저가 삭제될경우 해당된 게시물과 댓글이 같이 삭제됨
    content = models.TextField() ##댓글은 화려하지 않게 텍스트 형식으로만 작성할 수 있게 만들었다.
    created_at = models.DateTimeField(auto_now_add=True) ## 작석일
    updated_at = models.DateTimeField(auto_now=True)  ##업데이트일

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'  ##  #comment하면 해당하는 comment화면을 찾아감 
        # Create your models here.

    def is_updated(self):
        return self.updated_at - self.created_at > timedelta(seconds = 1)

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists(): #구글 사용자일시 구글프로필을 보여준다.
            return self.author.socialaccount_set.first().get_avatar_url()#장고에서 제공하는 기능인데 해당 사용자의 프로필 사진을 get하여 return해준다.
        else:
            return f'https://doitdjango.com/avatar/id/1209/d5a4ca79078b2e40/svg/{self.author.email}' #아닐시에 랜덤으로 나타나는 기본프로필를 보여준다.