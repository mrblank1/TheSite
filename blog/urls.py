from django.urls import path
from blog.views import  *
from blog.feeds import LatestEntriesFeed
app_name='blog'
urlpatterns = [
    path('' , blog_view, name='index'),
    path('<int:pid>' , blog_single, name='single'),
    path('single' , blog_single, name='single'),
    
    # path('category/<str:cat_name>' , blog_category, name='category'),
    path('tag/<str:tag_name>',blog_view, name='tag'),
    path('category/<str:cat_name>' , blog_category, name='category'),
    path('author/<str:aut_name>' , blog_author, name='author'),
    path('search/', blog_search, name='search'),
    path('rss/feed',LatestEntriesFeed())
]
