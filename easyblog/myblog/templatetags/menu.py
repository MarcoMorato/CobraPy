from django import template
from myblog.models import Category

register = template.Library()


@register.inclusion_tag('category_tpl.html')
def show_menu():
    category = Category.objects.all()
    return {"category": category}
