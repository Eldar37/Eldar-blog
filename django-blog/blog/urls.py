from django.urls import path
from . import views

urlpatterns = [
    # CRUD для категорий
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:id>/edit/', views.category_update, name='category_update'),
    path('categories/<int:id>/delete/', views.category_delete, name='category_delete'),

    # CRUD для постов
    path('', views.post_list, name='post_list'),  # главная страница
    path('posts/add/', views.post_create, name='post_create'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/<int:id>/edit/', views.post_update, name='post_update'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
]
