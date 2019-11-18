from . import views
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/register', views.register, name="register"),
]