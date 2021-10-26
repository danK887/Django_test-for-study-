from django import template
from mens.models import *

register = template.Library()

@register.simple_tag(name= 'getcats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('mens/list_categories.html')
def show_categories(sort=None, cat_celected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_celected': cat_celected}
