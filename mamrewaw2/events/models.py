from django.db import models

class Location(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=500, blank=True)
    info = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.title

class Event(models.Model):
    start_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=2000, blank=True)
    show_time = models.BooleanField()
    location = models.ForeignKey(Location, blank=True, null=True)

    def start(self):
        if self.show_time:
            return self.start_date
        else:
            return self.start_date.date()

    def __unicode__(self):
        return str(self.start()) + ' - ' + self.title