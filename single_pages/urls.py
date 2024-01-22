from django.urls import path
from . import views

urlpatterns = [
    path('site_introduction/', views.site_introduction),
    path('', views.landing),
]
