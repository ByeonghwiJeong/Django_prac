from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

# from django.conf import global_settings
# from askcompany import settings
# global_setting에 우리가 만든 settings를 Overwrite하기에 아래처럼 import
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include('instagram.urls')),
]

# DEBUG : 개발모드일때 True
# 업로드한 사진을 접근위해서
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)