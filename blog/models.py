from django.db import models
from django.contrib.auth.models import User
import os
from markdown import markdown
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

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

    def get_content_markdown(self):
        return markdown(self.content)


# Create your models here.

