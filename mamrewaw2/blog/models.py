from django.db import models

# Create your models here.
class RecordingSet(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def recordings(self):
        return self.recording_set.all()

class Recording(models.Model):
    title = models.CharField(max_length=200)
    content = models.FileField(upload_to='blog/recordings')
    type = models.CharField(max_length=200)
    set = models.ForeignKey(RecordingSet)

    def __unicode__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    img = models.ImageField(upload_to='blog/photos', blank=True, null=True)
    lead = models.CharField(max_length=2000)
    text = models.TextField()
    recordingSet = models.ForeignKey(RecordingSet, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def recordings(self):
        if self.recordingSet:
            return self.recordingSet.recording_set.all()
        else:
            return []

class Photo(models.Model):
    post = models.ForeignKey(Post)
    content = models.ImageField(upload_to='blog/photos')