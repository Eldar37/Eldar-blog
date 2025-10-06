from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'blog/category_form.html', {'form': form})

def category_update(request, id):
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'blog/category_form.html', {'form': form})

def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'blog/category_confirm_delete.html', {'category': category})

from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Список всех постов
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Детальная страница поста
def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

# Создание поста
@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        form.save_m2m()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'form': form})

# Редактирование поста
@login_required
def post_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'form': form})

# Удаление поста
@login_required
def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})



# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             form.save_m2m()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#         return render(request, 'blog/post_form.html', {'form': form})


# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             # post = form.save(commit=False)
#             # post.author = request.user
#             # post.save()
#             form.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#         return render(request, 'blog/post_form.html', {'form': form})

# C_R_UD

# Post.objects.all()
# Post.objects.get(id=1)
# Post.objects.filter()
# author = User.objects.get(username='pushkin')
# Filters :
    # contains 
    # exact =
    # startwith
    # endwith 
    # gt >
    # gte >=
    # lt < 
    # lte <=
