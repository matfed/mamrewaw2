from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='blog/photos', null=True)
    lead = models.CharField(max_length=2000)
    text = models.TextField()

    def __unicode__(self):
        return self.title

    def recordings(self):
        return self.recording_set.all()

class Photo(models.Model):
    post = models.ForeignKey(Post)
    content = models.ImageField(upload_to='blog/photos')

class Recording(models.Model):
    title = models.CharField(max_length=200)
    content = models.FileField(upload_to='blog/recordings')
    type = models.CharField(max_length=200)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.title