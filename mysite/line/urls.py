from django.urls import path
from .views import *
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.show),
    #path('f/', views.show)
    path('<str:post_id>/', views.show_post),
    #path('<str:post_id>/', views.show_post),
    #path('<str:post_id>/f/', views.show_post_guest),
    path('profile/<slug:user_slug>/', views.show_profile),

    path('api/post/<int:post_id>/like/', LikeDetail.as_view(), name='like'),
    #path('api/post/<int:id>/unlike/', UnlikeView.as_view(), name='unlike'),
    #path('api/postlist', PostAPIView.as_view()),
    #path('like_unlike/', views.like_unlike_post, name='like_unlike_post'),
]

