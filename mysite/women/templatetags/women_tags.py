from django import template
import women.views as views
from women.models import Category, TagPosts

register = template.Library()


@register.simple_tag()
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def show_categories(selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'selected': selected}


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {'tags': TagPosts.objects.all()}
