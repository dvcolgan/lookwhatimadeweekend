from django.contrib import admin
from themevoting.models import Theme, ThemeBump, Vote

admin.site.register(Theme)
admin.site.register(ThemeBump)
admin.site.register(Vote)