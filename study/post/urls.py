from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PostCreateView


router = DefaultRouter()
router.register('posts', views.PostViewSet)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('', views.main, name='main'),
]


