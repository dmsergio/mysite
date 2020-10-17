from django import template
from ..models import Post


register = template.Library()

@register.simple_tag(name='total_posts')
def get_total_published_posts():
    return Post.published.count()
