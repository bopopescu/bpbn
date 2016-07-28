from datetime import date

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import FieldTracker
from model_utils.fields import StatusField
from model_utils import Choices


class Country(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Salutation(models.Model):
    name = models.CharField(max_length=100)

    STANDARD_SALUTATION = 1

    def __str__(self):
        return self.name


class Gender(models.Model):
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.gender


class AgeCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PoliticalFuntion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


# class Bloodline(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.CharField(max_length=100, blank=True)
#     parent_clan = models.ForeignKey(Clan, blank=True, )
#
#     def __str__(self):
#         return self.name + " descending from " + self.parent_clan.name

# class Discipline(models.Model):
#     name = models.CharField(max_length=100)
#     clan = models.ForeignKey('Clan', related_name='clan')
#
#     def __str__(self):
#         return self.name


class Sect(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    salutation = models.ForeignKey(Salutation, default=Salutation.STANDARD_SALUTATION)
    domain = models.ForeignKey('Domain', related_name='person_domain', default=1)
    country = models.ForeignKey(Country)
    image = models.ImageField(blank=True)
    date_of_birth = models.DateField()
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name() + ", " + str(self.country)


class Event(models.Model):
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    country = models.ForeignKey(Country)
    gm = models.ForeignKey('Person', related_name='gm')
    substitute = models.ForeignKey('Person', related_name='substitute')

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('PropertyType', related_name='type')
    domain = models.ForeignKey('Domain', related_name='property_domain', default=1)
    initial = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.name


class Clan(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100, blank=True)
    # bloodline = models.BooleanField(default=0)
    parent = models.ForeignKey('Clan', related_name='parentclan', blank=True, null=True)
    disciplines = models.ManyToManyField(Property, through='ClanProperty')

    def __str__(self):
        return self.name


class ClanProperty(models.Model):
    clan = models.ForeignKey(Clan)
    property = models.ForeignKey(Property)

    def __str__(self):
        return self.clan.name + " " + self.property.name


class Character(models.Model):
    player = models.ForeignKey('Person', on_delete=models.CASCADE, default=1)
    salutation = models.ForeignKey(Salutation, default=1)
    nickname = models.CharField(max_length=200, blank=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, blank=True)
    generation = models.IntegerField(default=12)
    clan = models.ForeignKey(Clan)
    sect = models.ForeignKey(Sect, default=1)
    date_of_birth = models.DateField(default=date.today)
    date_of_death = models.DateField(default=date.today)
    gender = models.ForeignKey(Gender, default=1)
    rank = models.ForeignKey(Rank, default=1)
    clan_rank = models.IntegerField(default=1)
    function = models.ForeignKey(PoliticalFuntion, default=6)
    age_category = models.ForeignKey(AgeCategory, default=1)
    willpower = models.IntegerField(default=5)
    humanity = models.IntegerField(default=5)
    frenzy = models.IntegerField(default=5)
    bloodpool = models.IntegerField(default=10)
    domain = models.ForeignKey('Domain', related_name='character_domain', default=1)
    active = models.BooleanField(default=True)
    sire = models.ForeignKey('Character', related_name='character_sire', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    properties = models.ManyToManyField(Property, through='CharacterProperty')

    def __str__(self):
        return self.salutation.name + " " + self.firstname + " " + self.lastname


class PropertyType(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey('Domain', related_name='propertytype_domain', default=1)
    xpmultiplier = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class CharacterProperty(models.Model):
    character = models.ForeignKey('Character', related_name='cp_character', on_delete=models.CASCADE)
    property = models.ForeignKey('Property', related_name='property', on_delete=models.CASCADE)
    value = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    tracker = FieldTracker(fields=['value'])

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + ", " + self.property.name + ": " + str(
            self.value)


class BoonCategory(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + str(self.weight)


class Boon(models.Model):
    STATUS = Choices('waiting', 'accepted', 'declined')
    master = models.ForeignKey(Character, related_name='master', blank=True, null=True)
    slave = models.ForeignKey(Character, related_name='slave')
    category = models.ForeignKey(BoonCategory, related_name='category')
    note = models.TextField(default="please fill out a short decription")
    approvedbygm = StatusField()
    #approvedbygm = models.BooleanField(default=False)
    approvedbygm_note = models.TextField(default="Place for additional notes")
    approvedbyslave = StatusField()
    #approvedbyslave = models.BooleanField(default=False)
    approvedbyslave_note = models.TextField(default="Place for additional notes")
    hash_slave = models.CharField(max_length=20, default="")
    hash_gm = models.CharField(max_length=20, default="")
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slave.firstname + " " + self.slave.lastname + " owes a " + self.category.name + " to " + self.master.firstname + " " + self.master.lastname


class Xpearned(models.Model):
    character = models.ForeignKey(Character, blank=False, default=1)
    value = models.IntegerField(blank=False, null=False, default=1)
    event = models.ForeignKey(Event, related_name='event', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + " earned " + str(
            self.value) + " at " + self.event.name


class Xpspent(models.Model):
    character = models.ForeignKey(Character, blank=False, default=1)
    oldvalue = models.IntegerField(blank=False, null=False, default=1)
    newvalue = models.IntegerField(blank=False, null=False, default=1)
    xpcost = models.IntegerField(blank=False, null=False, default=1)
    property = models.ForeignKey(Property, blank=False, default=1)
    created = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.character.firstname + " " + self.character.lastname + " spent " + self.value + " on " + self.property.name


################################ GENEALOGY ################################

class Vampire(models.Model):
    name = models.CharField(max_length=100)
    sire = models.ForeignKey('Vampire', related_name='master', blank=True, null=True)
    generation = models.IntegerField(default=10, blank=True)
    columnStart = models.IntegerField(default=0, blank=True)
    columnEnd = models.IntegerField(default=0, blank=True)
    clan = models.ForeignKey('Clan', related_name='homeclan', blank=True, null=True)

    def __str__(self):
        return self.name
