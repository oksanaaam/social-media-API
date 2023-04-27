from django.contrib import admin

from social_media.models import Post, Like, Comment, Profile

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Profile)
