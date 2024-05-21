from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import PostForm, PostImageForm
from .models import Post, PostImage

# 게시물 관련 뷰
def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        
        post = Post.objects.create(
            title=title,
            text=text
        )
        images = request.FILES.getlist('image')
        for img in images:
            PostImage.objects.create(post=post, image=img)
            
        return redirect('main')
    else:
        return render(request, 'write.html')
    
def main(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'main.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    images = PostImage.objects.filter(post=post)
    return render(request, 'detail.html', {'post': post, 'images': images})

# 계정 관련 뷰
import pdb; pdb.set_trace()

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

# 로그인 뷰 (Django 기본 인증 뷰 사용)
login_view = auth_views.LoginView.as_view(template_name='login.html')

# 로그아웃 뷰 (Django 기본 인증 뷰 사용)
logout_view = auth_views.LogoutView.as_view()
