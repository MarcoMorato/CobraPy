from django import template
from myblog.models import Category, Post

register = template.Library()


@register.inclusion_tag('popular_posts_tpl.html')
def get_popular_posts():
    posts = Post.objects.order_by('-views')[:3]
    return {"posts": posts}
