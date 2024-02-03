from django.shortcuts import render ,get_object_or_404
from django.utils import  timezone
from blog.models import Post,Category,Comment
from blog.forms import CommentForm
# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
def blog_view(request):
    now = timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=1)
    categories = Category.objects.filter(post__in=posts).distinct() 
    try:
        posts=Paginator(posts,3)    
        page_num=request.GET.get('page')
        posts=posts.get_page(page_num)
    except PageNotAnInteger :
        posts=posts.get_page(1)
    except EmptyPage :
        posts=posts.get_page(1)
    context={'posts':posts,
             'categories':categories,
             }

    return render(request, 'blog/blog.html',context)
def blog_single(request,pid=1):
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS , "your submitted successfully")
        else:
            messages.add_message(request, messages.ERROR , "your comment did not validate")
    form=CommentForm()
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)  
    categories = Category.objects.filter(post__in=posts).distinct()  
    post=get_object_or_404(posts,pk=pid)
    comments = Comment.objects.filter(post=post.id,approved=True).order_by('-created_date')
    previous_post = posts.filter(pk__lt=post.pk).order_by('-pk').first()
    next_post = posts.filter(pk__gt=post.pk).order_by('pk').first()
    prev_next = {
        'previous': previous_post,
        'next': next_post,
        
    }
    post.counted_views+=1
    post.save()
    context={'post':post,
             'prev_next':prev_next,
             'categories':categories,
             'comments':comments,
             'form':form,
             }
    return  render(request, 'blog/blog-single.html',context)

def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    categories = Category.objects.filter(post__in=posts).distinct()
    posts=posts.filter(category__name=cat_name)
    try:
        posts=Paginator(posts,3)    
        page_num=request.GET.get('page')
        posts=posts.get_page(page_num)
    except PageNotAnInteger :
        posts=posts.get_page(1)
    except EmptyPage :
        posts=posts.get_page(1)
    context={'posts':posts,
             'categories':categories,
             }
    return render(request,'blog/blog.html',context)
def blog_author(request,aut_name):
    posts=Post.objects.filter(status=1)
    categories = Category.objects.filter(post__in=posts).distinct()
    posts=posts.filter(author__username = aut_name)

    try:
        posts=Paginator(posts,3)    
        page_num=request.GET.get('page')
        posts=posts.get_page(page_num)
    except PageNotAnInteger :
        posts=posts.get_page(1)
    except EmptyPage :
        posts=posts.get_page(1)
    context={'posts':posts,
             'categories':categories,
             }
    return render(request,'blog/blog.html',context)
def blog_search(request):
    

    now = timezone.now()
    posts=Post.objects.filter(published_date__lte=now,status=1)
    if request.method == 'GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    categories = Category.objects.filter(post__in=posts).distinct() 
    try:
        posts=Paginator(posts,3)    
        page_num=request.GET.get('page')
        posts=posts.get_page(page_num)
    except PageNotAnInteger :
        posts=posts.get_page(1)
    except EmptyPage :
        posts=posts.get_page(1)
    context={'posts':posts,
             'categories':categories,
             }

    return render(request, 'blog/blog.html',context)