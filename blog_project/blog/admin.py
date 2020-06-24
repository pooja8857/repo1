from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','author','body','publish','created','updated','status']
    list_filter = ('status','author','created','updated')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title','body']
    # raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','email','body','created','updated','active')
    list_filter = ('created','updated','active')
    search_fields = ('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


