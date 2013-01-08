from django.db import models

class Page(models.Model):
    url = models.CharField(max_length=200, primary_key=True)

    def __unicode__(self):
        return self.url

class Infobox(models.Model):
    text = models.CharField(max_length=2000)
    link = models.CharField(max_length=200, blank=True)
    position = models.FloatField()
    pages = models.ManyToManyField(Page, blank=True)

    def __unicode__(self):
        if len(self.text) < 200:
            return self.text
        else:
            return self.text[0:200] + "..."

    class Meta:
        ordering = ('position',)