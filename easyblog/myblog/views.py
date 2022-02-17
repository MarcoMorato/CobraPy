from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
from django.db.models import F


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
    template_name = 'single.html'
    context_object_name = 'item'

    # pk_url_kwarg = 'single_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
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
    category = Category.objects.all()
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['category'] = self.category
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
