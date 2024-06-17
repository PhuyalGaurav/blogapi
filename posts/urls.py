from django.urls import path

from .views import PostListCreate, PostRetrieveUpdateDestroy

urlpatterns = [
    path("<int:pk>/", PostRetrieveUpdateDestroy.as_view(), name="post_detail"),
    path("", PostListCreate.as_view(), name="post_list"),
]
