from django.test import TestCase
from blog.models import Article
from django.contrib.auth.models import User
from .base import UnitTest
from resume.forms import ResumeItemForm
from resume.models import ResumeItem


class TemplateTest(UnitTest):
    def test_home_page_returns_correct_template(self):
        self.set_up()
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/featured.html')

    def test_all_articles_page_returns_correct_template(self):
        self.set_up()
        response = self.client.get('/articles')
        self.assertTemplateUsed(response, 'blog/all_articles.html')

    def test_article_detail_page_returns_correct_template(self):
        self.set_up()
        response = self.client.get('/article/1/')
        self.assertTemplateUsed(response, 'blog/article_detail.html')

    def test_resume_page_return_correct_template(self):
        self.set_up()
        response = self.client.get('/resume/')
        self.assertTemplateUsed(response, 'resume/resume.html')


class ResumeNewItemTest(UnitTest):
    def test_resume_new_correct_template_returned(self):
        self.set_up()
        response = self.client.get('/resume/new')
        self.assertTemplateUsed(response, 'resume/new_resume_item.html')

    def test_resume_new_uses_form(self):
        self.set_up()
        response = self.client.get('/resume/new')
        self.assertIsInstance(response.context['form'], ResumeItemForm)

    def test_can_display_skill(self):
        self.set_up()
        ResumeItem.objects.create(section="SK", title="New Skill")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Skill')
