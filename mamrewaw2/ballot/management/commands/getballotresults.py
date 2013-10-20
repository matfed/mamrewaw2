from django.core.management.base import NoArgsCommand
from django.db.models import Count
from ballot.models import Vote
from ballot.models import Candidate

class Command(NoArgsCommand):
    help = "Getting ballot results"
    def handle_noargs(self, **options):
        candidates = Candidate.objects.annotate(num_votes=Count('vote')).order_by('-num_votes')
        for c in candidates:
            print "{0.name}\t{0.num_votes}".format(c)

        