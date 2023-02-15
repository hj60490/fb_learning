from django.contrib import admin
from fb_post.models import Post, Comment, React

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(React)

