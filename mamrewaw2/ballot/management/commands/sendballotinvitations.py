from django.core.management.base import NoArgsCommand
from ballot.models import Voter
from django.core.mail import send_mass_mail

class Command(NoArgsCommand):
    help = "Sending ballot invitations"
    def handle_noargs(self, **options):
        subject = "Internetowe wybory koordynatorow"
        from_email = "wybory@mamre.warszawa.pl"
        voters = Voter.objects.all().filter(used=False)
        print ('Sending email to: ')
        print (', '.join([voter.name for voter in voters]))
        datatuple = ((subject, generateMessage(voter), from_email, [voter.email]) for voter in voters)
        send_mass_mail(datatuple)


def generateMessage(voter):
    return u"""
Witaj, {0.name}

Aby zaglosowac na koordynatorow, wejdz na ponizsza strone:

http://mamre.warszawa.pl/ballot/landing/{0.token}/

i wprowadz swoj PIN:

{0.pin}

Powyzszy adres jak i nr PIN jest zindywidualizowany dla kazdego glosujacego i moze byc uzyty tylko raz.
Dane pozwalajace na identyfikacje glosow nie zostana zapisane w bazie.

Z pozdrowieniami,
Mateusz Fedoryszak
""".format(voter)
