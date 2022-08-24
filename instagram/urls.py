from . import views
from django.urls import path, re_path, register_converter

# 
class YearConverter:
    regex = r"20\d{2}"
    def to_python(self, value): # url로부터 추출한 문자열
        return int(value)
    def to_url(self, value): # url reverse 시에 호출
        return '%04d' % value

register_converter(YearConverter,'year') 

app_name = 'instagram' # URL Reverse에서 namespace역할을 하게 됩니다.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('archives/<int:year>/', views.archives_year),
    # 20XX 만 정규 표현식 match
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year),
    path('archives/<year:year>/', views.archives_year),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
]

