from selenium import webdriver
from .base import FunctionalTest
import time


class NewVisitorTest(FunctionalTest):
    def test_can_access_main_website(self):
        # Ellie has heard that a friend of hers has published a website
        # where he writes blogposts and hosts a personal CV. She goes
        # to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # She notices the page title and header mention a blog and a resume
        self.assertIn('Blog and Resume', self.browser.title)

        # Ellie is then prompted with a page with a featured article
        # and multiple side articles
        self.can_see_on_page('-featured-article')
        self.can_see_on_page('-side-article')

    def test_can_access_all_articles(self):
        self.browser.get('http://127.0.0.1:8000')

        # She also sees that there is a button to view all articles
        # underneath the side articles
        self.can_see_on_page('View all articles')
        view_all_articles_button = self.browser.find_element_by_id(
            "view-all-articles")

        # When Ellie clicks on it, she views a list of all articles
        view_all_articles_button.click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))
        self.assertIn('articles', self.browser.current_url)
        self.can_see_on_page('All articles')
        self.can_see_on_page('-side-article')

        # At the bottom of the list, there is a button that prompts
        # her back to the home page
        self.browser.find_element_by_class_name("-home-button").click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))
        self.can_see_on_page('-featured-article')
        self.can_see_on_page('-side-article')

    def test_can_access_article_details(self):
        self.browser.get('http://127.0.0.1:8000')

        # When Ellie clicks on an article, she is prompted with a page
        # containing the article details and text
        self.browser.find_element_by_class_name("-featured-article").click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))
        self.assertIn('article/', self.browser.current_url)
        self.can_see_on_page('-article-text')

        # At the bottom of the list, she again finds a button that prompts
        # her back to the home page
        self.browser.find_element_by_class_name("-home-button").click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))
        self.can_see_on_page('-featured-article')
        self.can_see_on_page('-side-article')

    def test_navbar(self):
        self.browser.get('http://127.0.0.1:8000')

        # Ellie notices the navbar
        self.assertIn(
            "navbar",
            self.browser.find_element_by_tag_name("body").get_attribute(
                'innerHTML'))

        # She sees that there is also an About section for the site
        self.can_see_in_navbar("About")

        # She also notices all other sections of the site listed in the navbar
        self.can_see_in_navbar("Articles")
        self.can_see_in_navbar("Resume")

    def test_can_access_about(self):
        # Ellie goes on the About section of the site
        self.browser.get('http://127.0.0.1:8000/about')

        # She is promped with some descriptive text about the project
        self.can_see_on_page('About the project')

        # She also notices a Source code button that points to GitHub
        self.can_see_on_page('-source-code-button')
        self.assertIn(
            "github",
            self.browser.find_element_by_class_name(
                "-source-code-button").get_attribute('href'))

        # And another that gets her back to the homepage
        self.browser.find_element_by_class_name("-home-button").click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))
        self.can_see_on_page('-featured-article')
        self.can_see_on_page('-side-article')
