from django.contrib import admin
from .models import Category, Tag, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.sites.site.register(Post)
admin.sites.site.register(Category)
admin.sites.site.register(Tag)