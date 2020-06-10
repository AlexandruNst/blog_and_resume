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
        # self.set_up()
        response = self.client.get('/articles')
        self.assertTemplateUsed(response, 'blog/all_articles.html')

    def test_article_detail_page_returns_correct_template(self):
        self.set_up()
        response = self.client.get('/article/1/')
        self.assertTemplateUsed(response, 'blog/article_detail.html')

    def test_resume_page_return_correct_template(self):
        # self.set_up()
        response = self.client.get('/resume/')
        self.assertTemplateUsed(response, 'resume/resume.html')


class ResumeNewItemTest(UnitTest):
    def test_resume_new_correct_template_returned(self):
        # self.set_up()
        response = self.client.get('/resume/new')
        self.assertTemplateUsed(response, 'resume/new_resume_item.html')

    def test_resume_new_uses_form(self):
        # self.set_up()
        response = self.client.get('/resume/new')
        self.assertIsInstance(response.context['form'], ResumeItemForm)

    def test_can_display_skill(self):
        # self.set_up()
        ResumeItem.objects.create(section="SK", title="New Skill")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Skill')

    def test_can_display_experience(self):
        # self.set_up()
        ResumeItem.objects.create(section="EX", title="New Experience")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Experience')

    def test_can_display_education(self):
        # self.set_up()
        ResumeItem.objects.create(section="ED", title="New Education")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Education')

    def test_can_display_technical_interest(self):
        # self.set_up()
        ResumeItem.objects.create(section="TI", title="New Technical-Interest")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Technical-Interest')

    def test_can_display_multiple_resume_items(self):
        # self.set_up()
        ResumeItem.objects.create(section="SK", title="New Skill")
        ResumeItem.objects.create(section="EX", title="New Experience")
        ResumeItem.objects.create(section="ED", title="New Education")
        ResumeItem.objects.create(section="TI", title="New Technical-Interest")
        response = self.client.get('/resume/')
        self.assertContains(response, 'New Skill')
        self.assertContains(response, 'New Experience')
        self.assertContains(response, 'New Education')
        self.assertContains(response, 'New Technical-Interest')

    def test_can_save_a_POST_request_to_resume(self):
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
        response = self.client.post(f'/resume/new',
                                    data={
                                        'section': 'SK',
                                        'title': 'New Skill',
                                        'timeframe': 'some time',
                                        'text': "Skill Text",
                                    })
        self.assertRedirects(response, '/resume/')

    def post_invalid_input(self):
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


class ResumeItemEditTest(UnitTest):
    def test_resume_edit_correct_template_returned(self):
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.get(f'/resume/{resume_item.id}/edit/')
        self.assertTemplateUsed(response, 'resume/new_resume_item.html')

    def test_resume_edit_uses_form(self):
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        response = self.client.get(f'/resume/{resume_item.id}/edit/')
        self.assertIsInstance(response.context['form'], ResumeItemForm)