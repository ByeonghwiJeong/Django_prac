from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()
    # get은 dict의 method key q가있을때는 가져오고 없을때는 빈문자열''반환
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list << 위치고정
    return render(request, 'instagram/post_list.html', {
        'post_list2': qs,
        'q': q
    })
    