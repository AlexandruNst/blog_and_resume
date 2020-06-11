from .base import UnitTest
from blog.models import Article
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class ArticleModelTest(UnitTest):
    def test_all_sections_must_be_filled(self):
        article = Article(author=None,
                          title='',
                          text='',
                          description='',
                          tags='',
                          created_date='')
        with self.assertRaises(ValidationError):
            article.save()
            article.full_clean()

    def test_article_list_ordering(self):
        user = User.objects.create_user('test_user', 'test@user.com',
                                        'mostsecurepasswordever')
        article1 = Article.objects.create(author=user)
        article2 = Article.objects.create(author=user)
        article3 = Article.objects.create(author=user)
        self.assertEqual(list(Article.objects.all()),
                         [article1, article2, article3])

    def create_dummy_article(self):
        user = User.objects.create_user('test_user', 'test@user.com',
                                        'mostsecurepasswordever')
        return Article.objects.create(author=user,
                                      title='title',
                                      text='text',
                                      description='description',
                                      tags='tag1 tag2 tag3')

    def test_default_time(self):
        article = self.create_dummy_article()
        self.assertAlmostEqual(article.created_date,
                               timezone.now(),
                               delta=timedelta(seconds=2))

    def test_string_representation(self):
        article = self.create_dummy_article()
        self.assertEqual(str(article), 'title')

    def test_get_list_of_tags(self):
        article = self.create_dummy_article()
        self.assertEqual(article.get_list_of_tags(),
                         ['#tag1', '#tag2', '#tag3'])