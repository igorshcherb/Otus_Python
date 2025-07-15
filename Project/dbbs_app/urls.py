from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("about/", views.AboutTemplateView.as_view(), name="about"),
    path("queries/", views.QueryListView.as_view(), name="query_list"),
    #     path('posts/add/', views.PostCreateView.as_view(), name='add_post'),
    #     path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    #     path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit_post'),
    #     path('authors/', views.author_list, name='author_list'),
    #
]
