from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),  # 새로운 URL 패턴 추가
    path('<int:post_id>/', views.detail, name='detail'),
]

