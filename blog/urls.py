from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about', views.About, name='about'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='blog'),
]