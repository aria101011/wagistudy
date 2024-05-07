from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, PostImage
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from rest_framework import viewsets

# View for rendering main page with all posts
def main(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'main.html', {'posts': posts})

# View for rendering post detail page
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})

# View for creating a new post
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            images = request.FILES.getlist('images')
            for image in images:
                PostImage.objects.create(post=post, image=image)
            return redirect('post:main')
    else:
        form = PostForm()
    return render(request, 'post/create.html', {'form': form})

# View for rendering list of posts (for REST API)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# View for creating a new post (for REST API)
@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# post/views.py
from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
