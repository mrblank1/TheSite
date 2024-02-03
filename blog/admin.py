
# Register your models here.
from django.contrib import admin
from blog.models import Post,Comment , Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display=('title','id','author', 'status','published_date')
    list_filter=('status','author' )
    summernote_fields = ('content',)
admin.site.register(Post,PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display=('name','id','approved','published_date')
    list_filter=('approved', )

admin.site.register(Category)