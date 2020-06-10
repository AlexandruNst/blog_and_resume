from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling_featured(self):
        #Ellie goes to the home page
        self.browser.get('http://127.0.0.1:8000')
        self.browser.set_window_size(1024, 768)

        #She notices the articles are nicely centered
        article_container = self.browser.find_element_by_css_selector(
            '.-article-container')
        self.assertAlmostEqual(article_container.location['x'] +
                               article_container.size['width'] / 2,
                               512,
                               delta=10)

    def test_layout_and_styling_all_articles(self):
        #Ellie goes to the article page
        self.browser.get('http://127.0.0.1:8000/articles')
        self.browser.set_window_size(1024, 768)

        #She notices the articles are nicely centered
        article_container = self.browser.find_element_by_css_selector(
            '.-article-container')
        self.assertAlmostEqual(article_container.location['x'] +
                               article_container.size['width'] / 2,
                               512,
                               delta=10)
