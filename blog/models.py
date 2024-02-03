from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django_summernote.fields import SummernoteTextField


# Create your models here.
class Category(models.Model):
        name=models.CharField(max_length=255)
        def __str__(self):
            return self.name
class Post(models.Model):

    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content=models.TextField()
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    login_required=models.BooleanField(default=False)
    category=models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField(null=True)
    # is_active=models.BooleanField(default=False)
    class Meta:
        ordering= ('created_date',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
         return reverse('blog:single', kwargs={'pid': self.id})

class Comment(models.Model):
     post=models.ForeignKey(Post,on_delete=models.CASCADE)
     name=models.CharField(max_length=255)
     email=models.EmailField()
     subject=models.CharField(max_length=255)
     message=models.TextField()
     created_date=models.DateTimeField(auto_now_add=True)
     published_date=models.DateTimeField(auto_now=True)
     approved=models.BooleanField(default=False)
     def __str__(self):
          return self.name