from django.contrib import admin
from .models import Post, Category, Tag, Comment, Menuname, Menulist

admin.site.register(Post)
admin.site.register(Comment)


#카테고리를 최종적으로 채워준다.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Menuname)
admin.site.register(Menulist)
