from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

# from django.conf import global_settings
# from askcompany import settings
# global_setting에 우리가 만든 settings를 Overwrite하기에 아래처럼 import
from django.conf import settings
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),
    path('', RedirectView.as_view(
        url = '/k-instagram/',
        pattern_name = 'instagram:post_list',
    ), name='root'), # root로 가면 /instagram 으로 Redirect
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('k-instagram/', include('instagram.urls')),
]

# DEBUG : 개발모드일때 True
# 업로드한 사진을 접근위해서
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]