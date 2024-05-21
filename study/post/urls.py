from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import write, main, detail, signup, home, login_view, logout_view

urlpatterns = [
    path('', main, name='main'),
    path('write/', write, name='write'),
    path('<int:post_id>/', detail, name='detail'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
