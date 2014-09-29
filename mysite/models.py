#coding=UTF-8
from django.db import models
from taggit.managers import TaggableManager

class Phrase(models.Model):
    """
    The Phrase model. The class is adding to django admin tool to allow basic CRUD operations.
    """
    title = models.CharField(max_length=256, help_text="Phrase title")
    month = models.IntegerField(default=15, help_text="Phrase month")
    day = models.IntegerField(default=15, help_text="Phrase day")
    body = models.TextField(blank=True, help_text="Phrase body")

    tags = TaggableManager()

    def __unicode__(self):
        return self.title


    class Meta:
        app_label = 'mysite'
