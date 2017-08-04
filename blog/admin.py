from django.contrib import admin
from .models import Category, Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.sites.site.register(Post, PostAdmin)
admin.sites.site.register(Category)
admin.sites.site.register(Tag)