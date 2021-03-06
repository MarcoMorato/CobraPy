import requests
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успещно зарегестрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def test(request):
    return render(request, 'test.html')


def test_content(request):
    posts = Post.objects.all()
    return render(request, 'test_content.html', {'posts': posts})


# def single(request, single_id):
#     post = Post.objects.get(pk=single_id)
#     return render(request, 'single.html', {'item': post})


class Content(ListView):
    model = Post
    template_name = 'test_content.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class Single(DetailView):
    model = Post
    # category = Category.objects.all()
    template_name = 'single.html'
    context_object_name = 'item'

    # pk_url_kwarg = 'single_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['category'] = self.category
        self.object.views = F('views') + 1  # для коректного прибавления просмотров
        self.object.save()
        self.object.refresh_from_db()  # для правильного отображения просмотров из базы данных
        return context


class Search(ListView):
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', {'posts': posts})


class Index(ListView):
    model = Post

    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        return context


class PostByCategory(ListView):
    model = Post

    template_name = 'category.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostByCategory, self).get_context_data()

        return context

    def get_queryset(self):
        return Post.objects.filter(categories_id=self.kwargs['categories_id'])

        # return Post.objects.filter(categories__pk=self.kwargs['pk'])


# def add_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             # post = Post.objects.create(**form.cleaned_data)
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request, 'add_post.html', {'form': form})


class AddPost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'add_post.html'

    # login_url = '/admin/'
    raise_exception = True
