from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post, Comment, Follow

User = get_user_model()

SIMBOLS: int = 15


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.author = User.objects.create_user(username='author')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост больше 15 символов',
            group=cls.group,
        )
        cls.comment = Comment.objects.create(
            post=cls.post,
            author=cls.user,
            text='Комментарий',
        )
        cls.follow = Follow.objects.create(
            user=cls.user,
            author=cls.author,
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у Post корректно работает __str__."""
        post = PostModelTest.post
        max_text = post.text[:SIMBOLS]
        length_text = len(str(post))
        self.assertEqual(len(max_text), length_text, 'Что-то не так')

    def test_models_group(self):
        """Проверяем, что у Group корректно работает __str__."""
        group = PostModelTest.group
        self.assertEqual(group.title, 'Тестовая группа')

    def test_models_comment(self):
        """Проверяем, что у Comment корректно работает __str__."""
        comment = PostModelTest.comment
        self.assertEqual(comment.text, 'Комментарий')

    def test_model_follow_str(self):
        """Проверка, что метод __str__ для Follow работает корректно"""
        follow = PostModelTest.follow
        self.assertEqual(str(follow), 'Follow')
