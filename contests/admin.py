from django.contrib import admin
from contests.models import Contest, Category, Submission, Rating


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'contest', 'receive_ratings', 'category')


admin.site.register(Contest)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Rating)
