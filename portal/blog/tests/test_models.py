from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post, Tag
from blog.tests.test_helpers import create_post, create_tag

User = get_user_model()


class ModelTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test-user')
        cls.tag = create_tag()
        cls.post = create_post(cls.user)

    def test_tag_model(self):
        """Проверяем, что тег создался с корректным значением name"""
        tag = Tag.objects.get(slug='slug')
        self.assertEqual(tag.name, 'test-name')

    def test_post_model(self):
        """Проверяем, что пост создался с корректным значением title"""
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'test')

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        object_verbose = {
            ModelTestCase.tag: f'{ModelTestCase.tag.name} - {ModelTestCase.tag.slug}',
            ModelTestCase.post: f'{ModelTestCase.post.author} - {ModelTestCase.post.pub_date} - {ModelTestCase.post.title}',
        }
        for obj, expected_value in object_verbose.items():
            with self.subTest(obj=obj):
                self.assertEqual(str(obj), expected_value)
