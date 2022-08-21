from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)#, validators=[]
    # 향후이 validators를 넣으면 숫자로만 이루어지게 유효성검사 추가가능