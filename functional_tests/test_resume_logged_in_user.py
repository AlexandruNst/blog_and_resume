from .base import FunctionalTest


class LoggedOutResumeUserTest(FunctionalTest):
    def test_resume_new(self):
        # Andy is a good friend of the creator of the app and
        # therefore has been provided credentials to log into it
        self.browser.get(self.live_server_url + '/admin')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('super_secret_password')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        # He goes to the resume page of the app
        self.browser.get(self.live_server_url + '/resume/')

        # He sees his friend's resume displayed
        self.can_see_on_page('-resume-container')

        # He can also see all 4 sections of the resume
        # listed with items in them
        self.can_see_on_page('skills')
        self.can_see_on_page('experience')
        self.can_see_on_page('education')
        self.can_see_on_page('technical_interests')

        # Andy notices the edit button at the bottom of the resume
        self.can_see_on_page('-edit-resume-button')

        # When he clicks on it, he can now add a resume item
        self.browser.find_element_by_class_name('-edit-resume-button').click()
        self.can_see_on_page('New Resume Item')

        # Andy has talked to his friend yesterday. He has been asked to
        # introduce a new entry into the resume, since his friend is busy
        # with some personal matters
        self.browser.find_element_by_xpath(
            "//select[@name='section']/option[text()='Skills']").click()
        self.browser.find_element_by_name("title").send_keys("Second skill")
        self.browser.find_element_by_name("timeframe").send_keys("last year")
        self.browser.find_element_by_name("text").send_keys("Something new")
        self.browser.find_element_by_class_name(
            '-resume-item-save-button').click()

        # Once he submits, he can see the new entry in the resume
        self.can_see_on_page('Second skill')
        self.can_see_on_page('last year')
        self.can_see_on_page('Something new')

    def test_resume_edit(self):
        # Andy is a good friend of the creator of the app and
        # therefore has been provided credentials to log into it
        self.browser.get(self.live_server_url + '/admin')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('super_secret_password')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        # He goes to the resume page of the app
        self.browser.get(self.live_server_url + '/resume/')

        # He sees his friend's resume displayed
        self.can_see_on_page('-resume-container')

        # He can also see all 4 sections of the resume
        # listed with items in them
        self.can_see_on_page('skills')
        self.can_see_on_page('experience')
        self.can_see_on_page('education')
        self.can_see_on_page('technical_interests')

        # Andy notices the edit link for each item in the sections
        self.can_see_on_page('-edit-link-edit')

        # He click on it and notices he can edit the resume item
        self.browser.find_element_by_class_name('-edit-link-edit').click()
        self.can_see_on_page('New Skill')
        self.can_see_on_page('past-present')
        self.can_see_on_page('Text')

        # His friend asked him to change the title of the item
        self.browser.find_element_by_name("title").clear()
        self.browser.find_element_by_name("title").send_keys("Best Skill Ever")
        self.browser.find_element_by_class_name(
            '-resume-item-save-button').click()

        # Then he can see that the resume page is updated
        self.cannot_see_on_page("New Skill")
        self.can_see_on_page('Best Skill Ever')

    def test_resume_delete(self):
        # Andy is a good friend of the creator of the app and
        # therefore has been provided credentials to log into it
        self.browser.get(self.live_server_url + '/admin')
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys(self.user.username)
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('super_secret_password')
        self.browser.find_element_by_xpath('//input[@value="Log in"]').click()

        # He goes to the resume page of the app
        self.browser.get(self.live_server_url + '/resume/')

        # He sees his friend's resume displayed
        self.can_see_on_page('-resume-container')

        # He can also see all 4 sections of the resume
        # listed with items in them
        self.can_see_on_page('skills')
        self.can_see_on_page('experience')
        self.can_see_on_page('education')
        self.can_see_on_page('technical_interests')

        # Andy notices the delete link for each item in the sections
        self.can_see_on_page('-edit-link-delete')

        # His friend asked him to delete one of the items
        # He clicks on the delete link and notices the item disappears from the resume
        self.browser.find_element_by_class_name('-edit-link-delete').click()
        self.cannot_see_on_page("New Skill")