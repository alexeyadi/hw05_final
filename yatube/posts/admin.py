from django.contrib import admin
from .models import Post, Group, Follow, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', )
    list_editable = ('group', )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


admin.site.register(Group, GroupAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Follow, FollowAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'created', 'author')
    search_fields = ('text',)
    empty_value_display = '-пусто-'
    list_filter = ('created',)


admin.site.register(Comment, CommentAdmin)
