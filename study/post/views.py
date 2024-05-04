from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.utils import timezone


# Create your views here.


    

def main(request):
    posts=Post.objects.all().order_by('-id')

    return render(request, 'main.html', {'posts':posts})

def detail(request, post_id):
    post=get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()  # 현재 시간으로 created_at 필드 설정
            post.save()
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})

