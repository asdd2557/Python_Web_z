from struct import pack
from django.urls import path
from blog import views

urlpatterns = [
   path('blog/delete_comment/<int:pk>/',views.delete_comment),
   path('blog/update_comment/<int:pk>/',views.CommentUpdate.as_view()),
   path('blog/update_post/<int:pk>/', views.PostUpdate.as_view()),
   path('blog/create_post/',views.PostCreate.as_view()),
   path('blog/tag/<str:slug>/',views.tag_page),
   path('blog/category/<str:slug>/', views.category_page),
   path('blog/<int:pk>/',views.PostDetail.as_view()),
   path('blog/',views.PostList.as_view()),
   path('',views.landing),
   path('about_me/',views.about_me),
   path('blog/<int:pk>/new_comment/', views.new_comment),
]
