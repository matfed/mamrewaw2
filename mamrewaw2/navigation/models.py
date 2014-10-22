from django.db import models

class MenuEntry(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    caption = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    position = models.FloatField()

    def __unicode__(self):
        return self.caption

    def check_if_selected(self, path):
        self.selected = path == self.link

    def children(self):
        return self.menuentry_set.order_by('position')
