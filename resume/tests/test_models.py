from .base import UnitTest
from resume.models import ResumeItem
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


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
