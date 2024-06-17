from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model

# Local
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
