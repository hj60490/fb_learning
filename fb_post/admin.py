from django.contrib import admin
from fb_post.models import Post, Comment, React, Person


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
    # list_filter = ('react__reaction', )
    # list_select_related = ('post', 'parent_comment')
    # search_fields = ['id']
    # raw_id_fields = ('post',)
    # readonly_fields = ('content',)
    # date_hierarchy = 'commented_at'
    # exclude = ('commented_by_id',)
    # fields = (('commented_by_id', 'content'), 'commented_at')


@admin.register(React)
class ReactAdmin(admin.ModelAdmin):
    pass

