from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', 'photo', 'tag_set', 'is_public'] 
        # Author 보여지지 않도록함, is_valid() 에서 유효성검사도 제외
        # exclude = []