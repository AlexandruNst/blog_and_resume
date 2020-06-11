from .base import FunctionalTest


class LoggedOutResumeUserTest(FunctionalTest):
    def test_resume(self):
        # Ellie goes to the resume page
        self.browser.get(self.live_server_url + '/resume/')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She notices her friend's resume is presented on screen
        self.can_see_on_page('-resume-container')

        # She can also see all 4 sections of the resume
        # listed with items in them
        self.can_see_on_page('skills')
        self.can_see_on_page('experience')
        self.can_see_on_page('education')
        self.can_see_on_page('technical_interests')

        # She doesn't seem to find any way to modify the resume entries,
        # which makes sense, since she is not an authorised user of the site
        # with an active account
        self.cannot_see_on_page('-edit-link')

        # At the bottom she notices a button which seems
        # would allow her to edit the resume
        self.can_see_on_page('-edit-resume-button')

        # However, right below it, Ellie sees that she needs to be logged in
        # in order to edit the resume
        self.can_see_on_page('Must be logged in to edit')

        # In spite of this, Ellie still clicks on the button
        self.browser.find_element_by_class_name('-edit-resume-button').click()
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # However, she is prompted with a login page
        self.can_see_on_page('Log in')

        # Since she doesn't have an account, she realises she really has
        # no way to edit her friend's resume. She goes back to the resume page
        self.browser.get(self.live_server_url + '/resume/')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))
        self.can_see_on_page('-resume-container')

        # Since Ellie knows a bit about how her friend's site might work,
        # she decides to try changing the URL to access that she should
        # have an account in order to access
        self.browser.get(self.live_server_url + '/resume/new')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She is immediately stopped by the log in screen again
        self.can_see_on_page('Log in')

        # She decides to try another possible URL that might give her
        # unauthorised access
        self.browser.get(self.live_server_url + '/resume/1/edit')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She is immediately stopped by the log in screen again
        self.can_see_on_page('Log in')

        # She decides to try one last time
        self.browser.get(self.live_server_url + '/resume/1/delete')
        self.wait_for(
            lambda: self.browser.find_elements_by_css_selector('.container'))

        # She is immediately stopped by the log in screen again
        self.can_see_on_page('Log in')

        # She realises there is no easy way to hack into her friend's app
