from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class BlogPostTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create(
            username = "testuser",
            email = "test@test.test",
            password = "test@testy??",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "Hello, Everyone This is a test post",
            body = "Nice Boobs with vey curvy waist mhm"
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Hello, Everyone This is a test post")
        self.assertEqual(self.post.body, "Nice Boobs with vey curvy waist mhm")
        self.assertEqual(self.post.active, True)
