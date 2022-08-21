from django.views.generic import ListView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Post

# --- CBV ---
post_list = ListView.as_view(model = Post)

# --- FBV ---
# def post_list(request):
#     qs = Post.objects.all()
#     # get은 dict의 method key q가있을때는 가져오고 없을때는 빈문자열''반환
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list << 위치고정
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q
#     })
    

# 타입힌트
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello World!")
    response.write("Hello World!")
    response.write("Hello World!")
    return response