from django.db import models


class ResumeItem(models.Model):
    SECTIONS = (
        ('SK', 'Skills'),
        ('EX', 'Experience'),
        ('ED', 'Education'),
        ('TI', 'Technical Interests'),
    )
    section = models.CharField(max_length=2, choices=SECTIONS)
    title = models.CharField(max_length=200)
    timeframe = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
