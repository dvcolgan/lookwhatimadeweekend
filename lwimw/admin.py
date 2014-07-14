from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from lwimw.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'contest', 'receive_ratings', 'category')

class PostAdmin(admin.ModelAdmin):
    list_filter = ('contest', 'author')
    list_display = ('author', 'contest', 'creation_date', 'title')

admin.site.register(Contest)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Rating)
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)
