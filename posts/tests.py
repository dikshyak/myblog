from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='tester', password='pass1234'
        )
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content here',
            author=self.user,
            published=True
        )

    def test_post_list_loads(self):
        r = self.client.get('/posts/')
        self.assertEqual(r.status_code, 200)

    def test_post_appears_in_list(self):
        r = self.client.get('/posts/')
        self.assertContains(r, 'Test Post')

    def test_post_detail_loads(self):
        r = self.client.get(f'/posts/{self.post.pk}/')
        self.assertEqual(r.status_code, 200)