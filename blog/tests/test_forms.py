from .base import UnitTest
from blog.forms import ArticleForm
from blog.models import Article


class ArticleFormTest(UnitTest):
    def test_form_renders_item_text_inputs(self):
        form = ArticleForm()
        self.assertIn('label for="id_author"', form.as_p())
        self.assertIn('name="author"', form.as_p())
        self.assertIn('label for="id_title"', form.as_p())
        self.assertIn('name="title"', form.as_p())
        self.assertIn('label for="id_description"', form.as_p())
        self.assertIn('name="description"', form.as_p())
        self.assertIn('label for="id_text"', form.as_p())
        self.assertIn('name="text"', form.as_p())
        self.assertIn('label for="id_tags"', form.as_p())
        self.assertIn('name="tags"', form.as_p())
        self.assertIn('label for="id_created_date"', form.as_p())
        self.assertIn('name="created_date"', form.as_p())
