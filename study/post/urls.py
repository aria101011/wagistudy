from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import write, main, detail, signup, home, login_view, logout_view

urlpatterns = [
    path('', main, name='main'),
    path('write/', write, name='write'),
    path('<int:post_id>/', detail, name='detail'),
    path('post/', include('post.urls')),  # 'post' 앱의 URL을 설정
    path('account/', include('account.urls')),  # 'accounts' 앱의 URL을 설정
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path, include


# post/urls.py
from django.urls import path
from . import views
from account.views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),  # account 앱의 signup 뷰로 연결
]

