from blog.models import Post
from django import template
from django.db.models import Count
register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_post123.html')
def show_latest_post(count=3):
    latest_post = Post.objects.order_by('-publish')[:count]
    return {'latest_post':latest_post}

@register.simple_tag(name='tags')
def get_most_commented_post(count=5):
    post=Post.objects.filter(total_comments=Count('comments')).order_by('-total_comments')[:count]
    print(post)
    return post