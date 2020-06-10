from .base import UnitTest
from resume.models import ResumeItem
from blog.models import Article


class ResumeItemModelTest(UnitTest):
    def test_default_text(self):
        resume_item = ResumeItem.objects.create(section="SK",
                                                title="New Skill")
        self.assertEqual(resume_item.timeframe, '')
        self.assertEqual(resume_item.text, '')