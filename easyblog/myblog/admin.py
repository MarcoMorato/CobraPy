from django.contrib import admin
from .models import Post, Tag, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categories', 'slug', 'photo', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)

