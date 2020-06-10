from django import forms

from .models import ResumeItem


class ResumeItemForm(forms.ModelForm):
    class Meta:
        model = ResumeItem
        fields = (
            "section",
            "title",
            "timeframe",
            "text",
        )
