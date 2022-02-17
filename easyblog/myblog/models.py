from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'categories_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=100)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    categories = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('single', kwargs={'single_id': self.pk})
        return reverse('single', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
