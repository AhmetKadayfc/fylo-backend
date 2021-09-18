from django.contrib import admin

from .models import Blog, Blog_Category, Tag

admin.site.register(Blog)
admin.site.register(Blog_Category)
admin.site.register(Tag)
