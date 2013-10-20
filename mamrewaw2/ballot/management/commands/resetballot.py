from django.core.management.base import NoArgsCommand
from ballot.models import *

class Command(NoArgsCommand):
    help = "Resets the ballot"
    def handle_noargs(self, **options):
        Vote.objects.all().delete()
        Voter.objects.all().delete()
        Candidate.objects.all().delete()
        Ballot.objects.all().delete()
        