from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "created",
        "updated",
        "active",
    ]
    search_fields = [
        "title",
        "body",
    ]
    list_filter = [
        "created",
        "updated",
        "active",
    ]
    list_editable = [
        "active",
    ]


admin.site.register(Post, PostAdmin)
