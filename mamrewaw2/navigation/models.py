from django.db import models

class MenuEntry(models.Model):
    caption = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    position = models.FloatField()

    def __unicode__(self):
        return self.caption

    def check_if_selected(self, path):
        self.selected = path == self.link
