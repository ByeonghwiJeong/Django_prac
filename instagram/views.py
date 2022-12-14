from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, ArchiveIndexView, \
    YearArchiveView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# @login_required # post.author = request.user >> 로그인 상황 보장 해야함
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False) # commit=False : instance.save의 호출을 지연시기키려고
#             post.author = request.user # 로그인 유저를 받아옴 
#             post.save() # 여기서 save()
#             messages.success(request, '포스팅을 저장했습니다')
#             return redirect(post)
#     else:
#         form = PostForm()

#     return render(request, 'instagram/post_form.html',{
#         'form': form,
#         'post': None,
#     })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스팅을 저장했습니다')
        return super().form_valid(form)

post_new = PostCreateView.as_view()

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
    
#     #작성자 Check Tip ~ 보통은 decorator로 하는것 추천 > 중복제거
#     if post.author != request.user:
#         messages.error(request, '작성자만 수정할 수 있습니다')
#         return redirect(post)

#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid(): 
#             post = form.save()
#             messages.success(request, '포스팅을 수정했습니다.')
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
    
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post,
#     })


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, '포스팅을 수정했습니다.')
        return super().form_valid(form)

post_edit = PostUpdateView.as_view()

# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, '포스팅을 삭제했습니다.')
#         return redirect('instagram:post_list')
#     return render(request, 'instagram/post_confirm_delete.html', {
#         'post': post,
#     })

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('instagram:post_list') 
    # 코드가 한줄한줄 읽힐때 reverse는 불가함 > reverse_lazy

    # def get_success_url(self):
    #     return reverse('instagram:post_list')

post_delete = PostDeleteView.as_view()


# --- CBV ---
# 가독성 안좋음
# post_list = login_required(ListView.as_view(model = Post, paginate_by =10))

# @method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 100

post_list = PostListView.as_view()
# --- F BV ---
# @login_required
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
#         'object': post,
#     })

# post_detail = DetailView.as_view(
#     model=Post,
#     queryset = Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(is_public=True)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated: # LoginOut인경우 Public만 보이기
            qs = qs.filter(is_public = True)
        return qs

post_detail = PostDetailView.as_view()


# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")

post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)