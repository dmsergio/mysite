from django import template
from django.db.models import Count

from ..models import Post


register = template.Library()

@register.simple_tag(name='total_posts')
def get_total_published_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    posts = Post.published.annotate(total_comments=Count('comments'))
    return posts.order_by('-total_comments')[:count]
