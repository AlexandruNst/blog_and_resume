from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling_featured(self):
        #Ellie goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        #She notices the articles are nicely centered
        article_container = self.browser.find_element_by_css_selector(
            '.-article-container')
        self.assertAlmostEqual(article_container.location['x'] +
                               article_container.size['width'] / 2,
                               512,
                               delta=10)

    def test_layout_and_styling_all_articles(self):
        #Ellie goes to the article page
        self.browser.get(self.live_server_url + '/articles')
        self.browser.set_window_size(1024, 768)
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        #She notices the articles are nicely centered
        article_container = self.browser.find_element_by_css_selector(
            '.-article-container')
        self.assertAlmostEqual(article_container.location['x'] +
                               article_container.size['width'] / 2,
                               512,
                               delta=10)

    def test_layout_and_styling_about(self):
        #Ellie goes to the about page
        self.browser.get(self.live_server_url + '/about')
        self.browser.set_window_size(1024, 768)
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        #She notices the content nicely centered
        article_container = self.browser.find_element_by_css_selector(
            '.-about-container')
        self.assertAlmostEqual(article_container.location['x'] +
                               article_container.size['width'] / 2,
                               512,
                               delta=10)

    def test_layout_and_styling_resume(self):
        #Ellie goes to the resume page
        self.browser.get(self.live_server_url + '/resume/')
        self.browser.set_window_size(1024, 768)
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        #She notices the resume nicely centered
        article_container = self.browser.find_element_by_css_selector(
            '.-resume-container')
        self.assertAlmostEqual(article_container.location['x'] +
                               article_container.size['width'] / 2,
                               512,
                               delta=10)
