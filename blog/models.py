from django.db import models
from django.conf import settings
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(blank=False)
    description = models.TextField(blank=False)
    tags = models.TextField(blank=False)
    image = models.CharField(max_length=200, blank=False)
    created_date = models.DateTimeField(default=timezone.now, blank=False)

    # published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title

    def get_list_of_tags(self):
        split_tags = self.tags.split()
        return ["#" + tag for tag in split_tags]

    def get_image(self):
        return "res/img/article_jpg/" + self.image + ".jpg"
