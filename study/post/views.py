from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, PostImage
from account.views import signup



# post/views.py
from django.shortcuts import render
from account.views import signup

def my_post_view(request):
    # 이 뷰에서 account 앱의 signup 뷰를 사용할 수 있습니다.
    # signup 뷰를 직접 호출하는 것이 아니라 필요한 로직을 호출하거나 리다이렉트할 수 있습니다.
    return render(request, 'signup.html')



@login_required
def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            post.save()
            images = request.FILES.getlist('image')
            for img in images:
                PostImage.objects.create(post=post, image=img)
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'write.html', {'form': form})

def main(request):
    if request.user.is_authenticated:
        # 현재 로그인한 사용자의 작성한 글만 가져옴
        posts = Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    return render(request, 'main.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    images = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {'post': post, 'images': images})


from django.shortcuts import render, redirect
from account.views import signup  # account 앱의 signup 뷰를 import

def my_view(request):
    # 필요한 로직 수행
    return redirect(signup)  # account 앱의 signup 뷰로 리다이렉트
