from django.contrib import admin
from .models import Post, Comments, Contact, Category


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'is_solved', 'created_at')
    list_display_links = ('id', 'full_name')




class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'is_published', 'view_count', 'created_at')
    list_display_links = ('id', 'title')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'is_published', 'created_at')
    list_display_links = ('id', 'name')


admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)