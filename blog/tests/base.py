from django.test import TestCase
from blog.models import Article
from django.contrib.auth.models import User


class UnitTest(TestCase):
    def set_up(self):
        user = User.objects.create_user('test_user', 'test@user.com',
                                        'mostsecurepasswordever')
        article1 = Article.objects.create(author=user)
        article2 = Article.objects.create(author=user)
        article3 = Article.objects.create(author=user)
        article4 = Article.objects.create(author=user)
        article5 = Article.objects.create(author=user)
        article6 = Article.objects.create(author=user)
