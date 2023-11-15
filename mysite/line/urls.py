from django.urls import path
from .views import LikeView, UnlikeView
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.show),
    path('<str:post_id>/', views.show_post),

    path('api/post/<int:id>/like/', LikeView.as_view(), name='like'),
    path('api/post/<int:id>/unlike/', UnlikeView.as_view(), name='unlike'),
    #path('like_unlike/', views.like_unlike_post, name='like_unlike_post'),
]

