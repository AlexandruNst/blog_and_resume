from .base import UnitTest
from resume.models import ResumeItem
from blog.models import Article
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class ResumeItemModelTest(UnitTest):
    def test_default_text(self):
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        self.assertEqual(resume_item.timeframe, '')
        self.assertEqual(resume_item.text, '')

    def test_cannot_save_resume_item_without_section_and_title(self):
        resume_item = ResumeItem(section='', title='')
        with self.assertRaises(ValidationError):
            resume_item.save()
            resume_item.full_clean()

    def test_resume_item_list_ordering(self):
        resume_item_1 = ResumeItem.objects.create(section="SK",
                                                  title="New Skill 1")
        resume_item_2 = ResumeItem.objects.create(section="SK",
                                                  title="Best Skill 2")
        resume_item_3 = ResumeItem.objects.create(section="SK",
                                                  title="Amazing Skill 3")
        self.assertEqual(list(ResumeItem.objects.all()),
                         [resume_item_1, resume_item_2, resume_item_3])

    def test_string_representation(self):
        resume_item_1 = ResumeItem.objects.create(section="SK",
                                                  title="New Skill 1")
        self.assertEqual(str(resume_item_1), 'New Skill 1')

    def test_has_text(self):
        resume_item_1 = ResumeItem.objects.create(section="SK",
                                                  title="New Skill 1",
                                                  text="Skill text")
        resume_item_2 = ResumeItem.objects.create(section="SK",
                                                  title="Best Skill 2")
        self.assertTrue(resume_item_1.has_text())
        self.assertFalse(resume_item_2.has_text())

    def test_get_text_lines(self):
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill 1",
                                                text="Line 1\nLine 2\nLine 3")
        self.assertEqual(resume_item.get_text_lines(), [
            'Line 1',
            'Line 2',
            'Line 3',
        ])


class ArticleModelTest(UnitTest):
    def test_all_sections_must_be_filled(self):
        article = Article(author=None,
                          title='',
                          text='',
                          description='',
                          tags='',
                          created_date='')
        with self.assertRaises(ValidationError):
            article.save()
            article.full_clean()

    def test_article_list_ordering(self):
        user = User.objects.create_user('test_user', 'test@user.com',
                                        'mostsecurepasswordever')
        article1 = Article.objects.create(author=user)
        article2 = Article.objects.create(author=user)
        article3 = Article.objects.create(author=user)
        self.assertEqual(list(Article.objects.all()),
                         [article1, article2, article3])

    def create_dummy_article(self):
        user = User.objects.create_user('test_user', 'test@user.com',
                                        'mostsecurepasswordever')
        return Article.objects.create(author=user,
                                      title='title',
                                      text='text',
                                      description='description',
                                      tags='tag1 tag2 tag3')

    def test_default_time(self):
        article = self.create_dummy_article()
        self.assertAlmostEqual(article.created_date,
                               timezone.now(),
                               delta=timedelta(seconds=2))

    def test_string_representation(self):
        article = self.create_dummy_article()
        self.assertEqual(str(article), 'title')

    def test_get_list_of_tags(self):
        article = self.create_dummy_article()
        self.assertEqual(article.get_list_of_tags(),
                         ['#tag1', '#tag2', '#tag3'])
