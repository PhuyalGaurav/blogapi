from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "title",
            "body",
            "author",
            "created",
            "active"
        ]
        model = Post