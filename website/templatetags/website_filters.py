from django import template
from blog.models import Post
register = template.Library()

@register.inclusion_tag('blog/recent-posts.html')
def recent_posts():
    posts=Post.objects.filter(status=True).order_by('published_date')[:6]
    return {'posts': posts}
