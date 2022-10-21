from django.contrib import admin
from blog.models import Article


# Register your models here.

# admin.site.register(Article)

@admin.register(Article)
class Article(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_main', 'created_at')
    list_display_links = ('id', 'title')
    list_editable = ('is_main',)
