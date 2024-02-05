from django import forms
from ckeditor.widgets import CKEditorWidget
from blog.models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # 이 부분을 제거

    class Meta:
        model = Post
        fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'codebox']
