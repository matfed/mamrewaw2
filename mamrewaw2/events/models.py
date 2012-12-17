import locale
from django.db import models

#locale.setlocale(locale.LC_TIME, 'pl_PL')

class Location(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=500, blank=True)
    info = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=500, blank=True)
    map = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.title

class Event(models.Model):
    MODE_CHOICES = (
        ('S', 'Shown'),
        ('H', 'Hidden'),
        ('O', 'Called off'),
    )
    start_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=2000, blank=True)
    show_time = models.BooleanField(default=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    mode = models.CharField(max_length=1, choices=MODE_CHOICES, default='S')

    def day_month(self):
        return str(self.start_date.day) + ' ' + int_to_roman(self.start_date.month)

    def start(self):
        if self.show_time:
            return self.start_date.strftime('%A, %d.%m.%Y %H:%M')
            #return self.start_date
        else:
            return self.start_date.strftime('%A, %d.%m.%Y')
            #return self.start_date.date()

    def __unicode__(self):
        return str(self.start()) + ' - ' + self.title

def int_to_roman(input):
   """
   Convert an integer to Roman numerals.

   Examples:
   >>> int_to_roman(0)
   Traceback (most recent call last):
   ValueError: Argument must be between 1 and 3999

   >>> int_to_roman(-1)
   Traceback (most recent call last):
   ValueError: Argument must be between 1 and 3999

   >>> int_to_roman(1.5)
   Traceback (most recent call last):
   TypeError: expected integer, got <type 'float'>

   >>> for i in range(1, 21): print int_to_roman(i)
   ...
   I
   II
   III
   IV
   V
   VI
   VII
   VIII
   IX
   X
   XI
   XII
   XIII
   XIV
   XV
   XVI
   XVII
   XVIII
   XIX
   XX
   >>> print int_to_roman(2000)
   MM
   >>> print int_to_roman(1999)
   MCMXCIX
   """
   if type(input) != type(1):
      raise TypeError, "expected integer, got %s" % type(input)
   if not 0 < input < 4000:
      raise ValueError, "Argument must be between 1 and 3999"   
   ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
   result = ""
   for i in range(len(ints)):
      count = int(input / ints[i])
      result += nums[i] * count
      input -= ints[i] * count
   return result


