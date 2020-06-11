from django.test import TestCase
from blog.models import Article
from .base import UnitTest


class ViewsTemplateTest(UnitTest):
    def test_home_page_returns_correct_template(self):
        self.set_up()
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/featured.html')

    def test_all_articles_page_returns_correct_template(self):
        response = self.client.get('/articles')
        self.assertTemplateUsed(response, 'blog/all_articles.html')

    def test_article_detail_page_returns_correct_template(self):
        self.set_up()
        response = self.client.get('/article/1/')
        self.assertTemplateUsed(response, 'blog/article_detail.html')

    def test_about_page_returns_correct_template(self):
        self.set_up()
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'blog/about.html')
