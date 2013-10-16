from ballot.models import Voter, Candidate, Vote
from django.contrib import admin

admin.site.register(Vote)
admin.site.register(Voter)
admin.site.register(Candidate)