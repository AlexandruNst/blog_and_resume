from .base import UnitTest
from resume.models import ResumeItem
from blog.models import Article
from django.core.exceptions import ValidationError


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