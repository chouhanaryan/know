from django.contrib import admin
from blog.models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)