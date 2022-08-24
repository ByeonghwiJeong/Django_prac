from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# 장고는 유저모델이 변경될 수 있기 때문에 다른 유저모델이 활성화 됐을수도 있음
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagmam/post/%Y%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True) 
    # Tag X 'Tag'문자열 O  // blank=True > 컬럼 추가시 필수
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f"Custom Post object ({self.id})"
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = '메세지글자수'

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args=[self.pk])
    

    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    # post_id 필드가 생성됨 
    # Post가 아닌 'Post' or 'instagram.Post' 문자열로 입력해도됨
    # Post : >> 다른 앱이면 import 해야함
    # 'Post' : 현재 instagram app 안에 있으므로 그안에 Post를 찾아서 참조
    # 'instagram.Post' : 다른앱에 모델을 직접 지정 - import 필요없음
    post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True})
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name