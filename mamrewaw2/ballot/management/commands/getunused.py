from django.core.management.base import NoArgsCommand
from ballot.models import Voter
from django.core.mail import send_mass_mail

class Command(NoArgsCommand):
    help = "Sending ballot invitations"
    def handle_noargs(self, **options):
        voters = Voter.objects.all().filter(used=False)
        print ('Haven\'t voted yet: ')
        print (', '.join([voter.name for voter in voters]))

