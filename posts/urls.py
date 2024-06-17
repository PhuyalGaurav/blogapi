from django.urls import path

from .views import PostListCreate, PostRetrieveUpdateDestroy, UserDetail, UserList

urlpatterns = [
    path("<int:pk>/", PostRetrieveUpdateDestroy.as_view(), name="post_detail"),
    path("", PostListCreate.as_view(), name="post_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("users/", UserList.as_view(), name="user_list"),
]
