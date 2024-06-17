from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"
