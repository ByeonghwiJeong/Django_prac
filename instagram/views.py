from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# --- CBV ---
post_list = ListView.as_view(model = Post)

# --- F BV ---
# def post_list(request):
#     qs = Post.objects.all()
#     # get은 dict의 method key q가있을때는 가져오고 없을때는 빈문자열''반환
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
    # # instagram/templates/instagram/post_list << 위치고정
    # return render(request, 'instagram/post_list.html', {
    #     'post_list': qs,
    #     'q': q
    # })
    

# post = get_object_or_404(Post, pk=pk)
# 아래와 같은 뜻
    # try:
    #     post = Post.objects.get(pk=pk) # DoseNotExist 예외
    # except Post.DoesNotExist:
    #     rais:
# 타입힌트  >>  (request: HttpRequest, pk: int) -> HttpResponse
# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html',{
#         'post': post,
#     })

post_detail = DetailView.as_view(model=Post)

def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")