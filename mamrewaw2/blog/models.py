from django.db import models
from slugify import slugify
from os import path

# Create your models here.
class RecordingSet(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.title + ' - ' + self.date.strftime('%d.%m.%Y')

    def recordings(self):
        return self.recording_set.all()


def recording_content_file_name(instance, filename):
    fileName, fileExtension = path.splitext(filename)
    return '/'.join(['blog', 'recordings', instance.set.date.strftime('%Y%m%d'), slugify(instance.title)[:64] + fileExtension])

class Recording(models.Model):
    title = models.CharField(max_length=200)
    content = models.FileField(upload_to=recording_content_file_name)
    type = models.CharField(max_length=200)
    set = models.ForeignKey(RecordingSet)

    def __unicode__(self):
        return unicode(self.set) + ' - ' + self.title

def post_img_file_name(instance, filename):
    fileName, fileExtension = path.splitext(filename)
    return '/'.join(['blog', 'photos', str(instance.pk), 'main' + fileExtension])

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    img = models.ImageField(upload_to=post_img_file_name, blank=True, null=True)
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