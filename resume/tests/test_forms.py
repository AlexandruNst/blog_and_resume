from .base import UnitTest
from resume.forms import ResumeItemForm
from resume.models import ResumeItem


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

    def test_validation_for_blank_section(self):
        form = ResumeItemForm(data={'section': '', 'title': 'Title'})
        self.assertFalse(form.is_valid())

    def test_validation_for_blank_title(self):
        form = ResumeItemForm(data={'section': 'SK', 'title': ''})
        self.assertFalse(form.is_valid())

    def test_validation_for_having_just_section_and_title(self):
        form = ResumeItemForm(data={'section': 'SK', 'title': 'Title'})
        self.assertTrue(form.is_valid())

    def test_form_save_handles_saving_to_db(self):
        form = ResumeItemForm(data={'section': 'SK', 'title': 'Title'})
        resume_item = form.save()
        self.assertEqual(resume_item, ResumeItem.objects.first())
        self.assertEqual(resume_item.title, 'Title')
        self.assertEqual(resume_item.section, "SK")