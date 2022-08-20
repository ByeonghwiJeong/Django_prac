from django.contrib import admin
from .models import Post

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
    list_display = ['id', 'message', 'message_length', 'is_public','created_at', 'updated_at']
    list_display_links = ['message']
    list_filter  = ['created_at', 'is_public']
    search_fields = ['message']
    
    def message_length(self, post):
        return len(post.message)