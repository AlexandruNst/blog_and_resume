from .base import FunctionalTest
from django.utils import timezone
from blog.models import Article
import time


class LoggedInBlogUserTest(FunctionalTest):
    def test_blog_new(self):
        # Andy is a good friend of the creator of the app and
        # therefore has been provided credentials to log into it
        self.browser.get(self.live_server_url + '/admin')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('super_secret_password')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        # He goes to the all articles page of the app
        self.browser.get(self.live_server_url + '/articles')

        # He sees his friend's articles displayed
        self.can_see_on_page('-article-container')

        # Andy notices the add button at the top of the blog
        self.can_see_on_page('-new-article-button')

        # When he clicks on it, he can now add an article
        self.browser.find_element_by_class_name('-new-article-button').click()
        self.can_see_on_page('Article')

        # Andy has talked to his friend yesterday. He has been asked to
        # introduce a new article, since his friend is busy
        # with some personal matters
        self.browser.find_element_by_xpath(
            "//select[@name='author']/option[text()='andy']").click()
        self.browser.find_element_by_name("title").send_keys("New Article")
        self.browser.find_element_by_name("description").send_keys(
            "New description")
        self.browser.find_element_by_name("text").send_keys("New Text")
        self.browser.find_element_by_name("tags").send_keys(
            "newtag1 newtag2 newtag3")
        self.browser.find_element_by_name("created_date").send_keys(
            str(timezone.now()))
        self.browser.find_element_by_class_name('-article-save-button').click()

        # Once he submits, he can see the new entry in the blog
        self.can_see_on_page('New Article')

    def test_blog_edit(self):
        # Andy is a good friend of the creator of the app and
        # therefore has been provided credentials to log into it
        self.browser.get(self.live_server_url + '/admin')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('super_secret_password')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        # He goes to the all articles page of the app
        self.browser.get(self.live_server_url + '/articles')
        self.browser.set_window_size(1800, 768)

        # He sees his friend's articles displayed
        self.can_see_on_page('-article-container')

        # Andy notices the edit link for each article
        self.can_see_on_page('-edit-link-edit')

        # He click on it and notices he can edit the article
        self.browser.find_element_by_class_name('-edit-link-edit').click()
        self.can_see_on_page('Title')
        self.can_see_on_page('Desc')
        self.can_see_on_page('Text')

        # His friend asked him to change the title of the article
        self.browser.find_element_by_name("title").clear()
        self.browser.find_element_by_name("title").send_keys("Completely New")
        self.browser.find_element_by_class_name('-article-save-button').click()

        # Then he can see that the article page is updated
        self.can_see_on_page('Completely New')

        # Oops! Andy realises his friend has missed a word in the title
        # of an article
        # He goes to the detail page of that article
        self.browser.find_element_by_class_name("-article-img").click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # He notices the wrong title when he clicks on the edit button
        self.browser.find_element_by_class_name('-edit-link-edit').click()

        # He corrects his mistake
        self.browser.find_element_by_name("title").clear()
        self.browser.find_element_by_name("title").send_keys(
            "Completely Brand New")
        self.browser.find_element_by_class_name('-article-save-button').click()

        # Then he can see that the article page is updated
        self.can_see_on_page('Completely Brand New')

    def test_blog_delete(self):
        # Andy is a good friend of the creator of the app and
        # therefore has been provided credentials to log into it
        self.browser.get(self.live_server_url + '/admin')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('super_secret_password')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        # He goes to the all articles page of the app
        self.browser.get(self.live_server_url + '/articles')
        self.browser.set_window_size(1800, 1800)

        # He sees his friend's articles displayed
        self.can_see_on_page('-article-container')
        number_of_articles = Article.objects.count()

        # Andy notices the delete link for each article
        self.can_see_on_page('-edit-link-delete')

        # His friend asked him to delete 2 of the articles
        # He clicks on the delete link of one and notices the
        # article disappears from the blog
        self.browser.find_element_by_class_name('-edit-link-delete').click()
        self.assertEqual(Article.objects.count(), number_of_articles - 1)

        # He then goes to the second article's detail page
        self.browser.find_element_by_class_name("-article-img").click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # He clicks on the delete link and notices the
        # article disappears from the blog
        self.browser.find_element_by_class_name('-edit-link-delete').click()
        self.assertEqual(Article.objects.count(), number_of_articles - 2)