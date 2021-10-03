from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)


class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'category', 'created')


admin.site.register(News, AdminNews)
