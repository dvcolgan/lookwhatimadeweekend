from django.contrib import admin
from blog.models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('contest', 'author')
    list_display = ('author', 'contest', 'creation_date', 'title')

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)