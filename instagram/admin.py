from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

# 1 번
# admin.site.register(Post)

# 2번
# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)

# 3번 - 추천 방법
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public','created_at', 'updated_at']
    list_display_links = ['message']
    list_filter  = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            # return f'<img src="{post.photo.url}" />'
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px"/>')
        return None
    
    def message_length(self, post):
        return len(post.message)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass