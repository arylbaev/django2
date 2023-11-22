from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *


def show(request):
    posts = Post.objects.all()

    return render(request, 'line.html', {'posts': posts})


def show_post_user(request, post_id, user_id):
    post = get_object_or_404(Post, pk=post_id)
    #user = get_object_or_404(CustomUser, pk=user_id)

    return render(request, 'line/post.html', {'post': post})


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    @action(detail=True, methods=['POST'])
    def set_like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': 'liked'})


def show_post_guest(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'line/post.html', {'post': post})


def like_post(request, post_id, user_id):
    user = CustomUser.objects.get(id=user_id)
    #like = Like(post_id, user_id)
    #like.save()
    post = get_object_or_404(Post, pk=post_id)
    Like.objects.create(post_liked=post, like_author=user)

    return render(request, 'line/post.html', {'post': post, 'user': user})

class LikeView(CreateAPIView):

    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs["id"])
        user = request.user
        like = Like.objects.create(post=post, user=user)

        return Response(LikeSerializer(like).data, status=status.HTTP_200_OK)


class UnlikeView(DestroyAPIView):

    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        user = request.user
        post = Post.objects.get(id=kwargs["id"])
        like = Like.objects.get(user=user, post=post)
        like.delete()

        return Response(status=status.HTTP_200_OK)


class PostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer






