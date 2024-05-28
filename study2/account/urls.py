from django.urls import path
from .views import *

urlpatterns =[
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
]


# 프로젝트의 urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),  # account 앱의 URL 패턴을 포함
    path('post/', include('post.urls')),  # post 앱의 URL 패턴을 포함
]
