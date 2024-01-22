from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.site_introduction),
    path('', views.landing),
]
##fdfff