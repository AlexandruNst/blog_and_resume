from django.test import TestCase
from blog.models import Article
from django.contrib.auth.models import User
from .base import UnitTest
from resume.forms import ResumeItemForm
from resume.models import ResumeItem


class ViewsTemplateTest(UnitTest):
    def test_resume_page_return_correct_template(self):
        response = self.client.get('/resume/')
        self.assertTemplateUsed(response, 'resume/resume.html')


class ResumeViewTest(UnitTest):
    def test_can_display_skill(self):
        ResumeItem.objects.create(section="SK", title="New Skill")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Skill')

    def test_can_display_experience(self):
        ResumeItem.objects.create(section="EX", title="New Experience")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Experience')

    def test_can_display_education(self):
        ResumeItem.objects.create(section="ED", title="New Education")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Education')

    def test_can_display_technical_interest(self):
        ResumeItem.objects.create(section="TI", title="New Technical-Interest")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Technical-Interest')

    def test_can_display_multiple_resume_items(self):
        ResumeItem.objects.create(section="SK", title="New Skill")
        ResumeItem.objects.create(section="EX", title="New Experience")
        ResumeItem.objects.create(section="ED", title="New Education")
        ResumeItem.objects.create(section="TI", title="New Technical-Interest")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Skill')
        self.assertContains(response, 'New Experience')
        self.assertContains(response, 'New Education')
        self.assertContains(response, 'New Technical-Interest')

    def test_resume_new_passes_correct_items_to_template(self):
        ResumeItem.objects.create(section="SK", title="New Skill")
        ResumeItem.objects.create(section="EX", title="New Experience")
        ResumeItem.objects.create(section="ED", title="New Education")
        ResumeItem.objects.create(section="TI", title="New Technical-Interest")

        skills = ResumeItem.objects.filter(section="SK")
        experience = ResumeItem.objects.filter(section="EX")
        education = ResumeItem.objects.filter(section="ED")
        technical_interests = ResumeItem.objects.filter(section="TI")

        response = self.client.get('/resume/')

        self.assertEqual(list(response.context['skills_list']), list(skills))
        self.assertEqual(list(response.context['experience_list']),
                         list(experience))
        self.assertEqual(list(response.context['education_list']),
                         list(education))
        self.assertEqual(list(response.context['technical_interests_list']),
                         list(technical_interests))


class ResumeItemNewViewTest(UnitTest):
    def test_resume_new_correct_template_returned(self):
        self.set_up_user()
        response = self.client.get('/resume/new')
        self.assertTemplateUsed(response, 'resume/new_resume_item.html')

    def test_resume_new_uses_form(self):
        self.set_up_user()
        response = self.client.get('/resume/new')
        self.assertIsInstance(response.context['form'], ResumeItemForm)

    def test_can_save_a_POST_request_to_resume(self):
        self.set_up_user()
        self.client.post(f'/resume/new',
                         data={
                             'section': 'SK',
                             'title': 'New Skill',
                             'timeframe': 'some time',
                             'text': "Skill Text",
                         })
        self.assertEqual(ResumeItem.objects.count(), 1)
        new_item = ResumeItem.objects.first()
        self.assertEqual(new_item.section, 'SK')
        self.assertEqual(new_item.title, 'New Skill')
        self.assertEqual(new_item.timeframe, 'some time')
        self.assertEqual(new_item.text, 'Skill Text')

    def test_resume_new_redirects_to_resume_view(self):
        self.set_up_user()
        response = self.client.post(f'/resume/new',
                                    data={
                                        'section': 'SK',
                                        'title': 'New Skill',
                                        'timeframe': 'some time',
                                        'text': "Skill Text",
                                    })
        self.assertRedirects(response, '/resume/')

    def post_invalid_input(self):
        self.set_up_user()
        return self.client.post(f'/resume/new',
                                data={
                                    'section': '',
                                    'title': '',
                                })

    def test_resume_new_invalid_input_not_saved(self):
        self.post_invalid_input()
        self.assertEqual(ResumeItem.objects.count(), 0)

    def test_resume_new_invalid_input_renders_new_item_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/new_resume_item.html')

    def test_resume_new_invalid_input_passes_form_to_template(self):
        response = self.post_invalid_input()
        self.assertIsInstance(response.context['form'], ResumeItemForm)


class ResumeItemEditViewTest(UnitTest):
    def test_resume_edit_correct_template_returned(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.get(f'/resume/{resume_item.id}/edit/')
        self.assertTemplateUsed(response, 'resume/new_resume_item.html')

    def test_resume_edit_uses_form(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.get(f'/resume/{resume_item.id}/edit/')
        self.assertIsInstance(response.context['form'], ResumeItemForm)

    def test_resume_edit_displays_item(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.get(f'/resume/{resume_item.id}/edit/')
        self.assertContains(response, "New Skill")

    def test_resume_edit_displays_correct_item(self):
        self.set_up_user()
        resume_item_1 = ResumeItem.objects.create(section="SK",
                                                  title="New Skill 1")
        resume_item_2 = ResumeItem.objects.create(section="SK",
                                                  title="Best Skill 2")
        response = self.client.get(f'/resume/{resume_item_1.id}/edit/')
        self.assertContains(response, "New Skill 1")
        self.assertNotContains(response, "Best Skill 2")

    def test_resume_edit_can_edit_item(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.get(f'/resume/{resume_item.id}/edit/')
        self.assertContains(response, "New Skill")

        response = self.client.post(f'/resume/{resume_item.id}/edit/',
                                    data={
                                        'section': 'SK',
                                        'title': 'Best Skill',
                                    })
        self.assertNotEqual(ResumeItem.objects.first().title, "New Skill")
        self.assertEqual(ResumeItem.objects.first().title, "Best Skill")

    def test_resume_edit_redirects_to_resume_view(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.post(f'/resume/{resume_item.id}/edit/',
                                    data={
                                        'section': 'SK',
                                        'title': 'Best Skill',
                                    })
        self.assertRedirects(response, '/resume/')

    def post_invalid_input(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        return self.client.post(f'/resume/{resume_item.id}/edit/',
                                data={
                                    'section': '',
                                    'title': '',
                                })

    def test_resume_edit_invalid_input_not_saved(self):
        self.post_invalid_input()
        self.assertEqual(ResumeItem.objects.first().title, "New Skill")

    def test_resume_edit_invalid_input_renders_new_item_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'resume/new_resume_item.html')

    def test_resume_edit_invalid_input_passes_form_to_template(self):
        response = self.post_invalid_input()
        self.assertIsInstance(response.context['form'], ResumeItemForm)

    def test_resume_edit_for_unknown_item_gives_404(self):
        self.set_up_user()
        response = self.client.post(f'/resume/101/edit/',
                                    data={
                                        'section': 'SK',
                                        'title': 'New Skill',
                                    })
        self.assertEqual(response.status_code, 404)


class ResumeItemDeleteViewTest(UnitTest):
    def test_resume_delete_redirects_to_resume_view(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.post(f'/resume/{resume_item.id}/delete/')
        self.assertRedirects(response, '/resume/')

    def test_resume_delete_successfully_deletes_item(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        self.assertEqual(ResumeItem.objects.count(), 1)
        response = self.client.post(f'/resume/{resume_item.id}/delete/')
        self.assertEqual(ResumeItem.objects.count(), 0)

    def test_resume_delete_deletes_correct_item(self):
        self.set_up_user()
        resume_item_1 = ResumeItem.objects.create(section="SK",
                                                  title="New Skill 1")
        resume_item_2 = ResumeItem.objects.create(section="SK",
                                                  title="Best Skill 2")
        self.assertEqual(ResumeItem.objects.count(), 2)
        response = self.client.post(f'/resume/{resume_item_1.id}/delete/')
        self.assertEqual(ResumeItem.objects.count(), 1)
        self.assertNotEqual(ResumeItem.objects.first().title, "New Skill 1")
        self.assertEqual(ResumeItem.objects.first().title, "Best Skill 2")

    def test_resume_delete_removes_item_from_resume_view(self):
        self.set_up_user()
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        resume = self.client.get('/resume/')
        self.assertContains(resume, "New Skill")
        response = self.client.post(f'/resume/{resume_item.id}/delete/')
        resume = self.client.get('/resume/')
        self.assertNotContains(resume, "New Skill")

    def test_resume_delete_removes_correct_item_from_resume_view(self):
        self.set_up_user()
        resume_item_1 = ResumeItem.objects.create(section="SK",
                                                  title="New Skill 1")
        resume_item_2 = ResumeItem.objects.create(section="SK",
                                                  title="Best Skill 2")
        resume = self.client.get('/resume/')
        self.assertContains(resume, "New Skill 1")
        self.assertContains(resume, "Best Skill 2")
        response = self.client.post(f'/resume/{resume_item_1.id}/delete/')
        resume = self.client.get('/resume/')
        self.assertNotContains(resume, "New Skill 1")
        self.assertContains(resume, "Best Skill 2")

    def test_resume_delete_for_unknown_item_gives_404(self):
        self.set_up_user()
        response = self.client.post(f'/resume/101/delete/')
        self.assertEqual(response.status_code, 404)