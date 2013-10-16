from django.db import models
import uuid
import random

def getPin():
    return ''.join([str(x) for x in random.sample(range(0,10),6)])

class Voter(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    token = models.CharField(max_length=32, default=lambda: uuid.uuid4().hex)
    pin = models.CharField(max_length=6, default=getPin)
    used = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.name

class Ballot(models.Model):
    def __unicode__(self):
        return str(self.id)

class Vote(models.Model):
    ballot = models.ForeignKey('Ballot')
    candidate = models.ForeignKey('Candidate')

    def __unicode__(self):
        return str(self.ballot.id) + " for " + self.candidate.name
