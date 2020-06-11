import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from django.contrib.auth.models import User
from django.test import Client
from blog.models import Article
from resume.models import ResumeItem
from django.utils import timezone
from selenium.webdriver.firefox.options import Options

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.options = Options()
        self.options.headless = True
        self.browser = webdriver.Firefox(options=self.options)
        self.client = Client()
        self.user = User.objects.create_superuser(
            username='andy',
            password='super_secret_password',
            email='andy@bestfriend.com',
            is_active=True)
        self.user.save()
        Article.objects.create(author=self.user,
                               title='Title',
                               description='Desc',
                               text='Text',
                               tags="tag1 tag2 tag3",
                               created_date=timezone.now())
        Article.objects.create(author=self.user,
                               title='Title',
                               description='Desc',
                               text='Text',
                               tags="tag1 tag2 tag3",
                               created_date=timezone.now())
        Article.objects.create(author=self.user,
                               title='Title',
                               description='Desc',
                               text='Text',
                               tags="tag1 tag2 tag3",
                               created_date=timezone.now())
        Article.objects.create(author=self.user,
                               title='Title',
                               description='Desc',
                               text='Text',
                               tags="tag1 tag2 tag3",
                               created_date=timezone.now())
        Article.objects.create(author=self.user,
                               title='Title',
                               description='Desc',
                               text='Text',
                               tags="tag1 tag2 tag3",
                               created_date=timezone.now())
        Article.objects.create(author=self.user,
                               title='Title',
                               description='Desc',
                               text='Text',
                               tags="tag1 tag2 tag3",
                               created_date=timezone.now())
        ResumeItem.objects.create(section="SK",
                                  title="New Skill",
                                  timeframe="past-present",
                                  text="Text")

    def tearDown(self):
        self.browser.quit()

    def can_see_on_page(self, search_item_name):
        content = self.browser.find_element_by_id('content').get_attribute(
            'innerHTML')
        self.assertIn(search_item_name, content)

    def cannot_see_on_page(self, search_item_name):
        content = self.browser.find_element_by_id('content').get_attribute(
            'innerHTML')
        self.assertNotIn(search_item_name, content)

    def can_see_in_navbar(self, search_item_name):
        content = self.browser.find_element_by_id('navbar').get_attribute(
            'innerHTML')
        self.assertIn(search_item_name, content)

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
