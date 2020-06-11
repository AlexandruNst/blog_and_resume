from .base import FunctionalTest


class LoggedOutBlogUserTest(FunctionalTest):
    def test_blog(self):
        # Ellie goes to the all articles page
        self.browser.get(self.live_server_url + '/articles')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She receives all existing articles
        self.can_see_on_page('-article-container')

        # She doesn't seem to find any way to modify the articles,
        # which makes sense, since she is not an authorised user of the site
        # with an active account
        self.cannot_see_on_page('-edit-link')

        # Since Ellie knows a bit about how her friend's site might work,
        # she decides to try changing the URL to access that she should
        # have an account in order to access
        self.browser.get(self.live_server_url + '/article/new')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She is immediately stopped by the log in screen
        self.can_see_on_page('Log in')

        # She decides to try another possible URL that might give her
        # unauthorised access
        self.browser.get(self.live_server_url + '/article/1/edit')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She is immediately stopped by the log in screen again
        self.can_see_on_page('Log in')

        # She decides to try one last time
        self.browser.get(self.live_server_url + '/article/1/delete')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She is immediately stopped by the log in screen again
        self.can_see_on_page('Log in')

        # She realises there is no easy way to hack into her friend's app

    def test_article_detail(self):
        # Ellie goes to the page detailing one of the articles
        self.browser.get(self.live_server_url + '/article/6/')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She receives all existing articles
        self.can_see_on_page('-article-text')

        # She doesn't seem to find any way to modify the articles,
        # which makes sense, since she is not an authorised user of the site
        # with an active account
        self.cannot_see_on_page('-edit-link')