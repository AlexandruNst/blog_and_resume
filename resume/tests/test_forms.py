from .base import UnitTest
from resume.forms import ResumeItemForm


class ResumeItemFormTest(UnitTest):
    def test_form_renders_item_text_inputs(self):
        form = ResumeItemForm()
        self.assertIn('label for="id_section"', form.as_p())
        self.assertIn('name="section"', form.as_p())
        self.assertIn('label for="id_title"', form.as_p())
        self.assertIn('name="title"', form.as_p())
        self.assertIn('label for="id_timeframe"', form.as_p())
        self.assertIn('name="timeframe"', form.as_p())
        self.assertIn('label for="id_text"', form.as_p())
        self.assertIn('name="text"', form.as_p())
