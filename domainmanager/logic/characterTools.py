import random
import string

from django.db import transaction
from django.db.models import Sum

from domainmanager.models import CharacterProperty, ClanProperty, Property, Xpearned, Xpspent


# Create initial character properties
# property types are:
# 1 ... Abilities
# 2 ... Attributes
# 3 ... Backgrounds
def createInitialProperties(character):
    properties = Property.objects.filter(domain__exact=character.domain).filter(initalizeatcharactercreation__exact=Property.STATUS.yes)

    # initialze all initalizecharactercreation properties with value = 1
    for property in properties:
        cp = CharacterProperty(character=character, property=property, value=1)
        cp.save()


def createInitialDisciplines(character):
    clanDisciplines = ClanProperty.objects.filter(clan__exact=character.clan)

    for discipline in clanDisciplines:
        cp = CharacterProperty(character=character, property=discipline.property, value=0)
        cp.save()


def getCharacterProportiesOfType(character, type):
    return CharacterProperty.objects.filter(character=character).filter(
        property__type__stattype__exact=type).order_by('property__initalizeatcharactercreation')


# immer das nächste Level
# Skills * 3
# Backgrounds * 4
# Attribute * 5
# disci clan * 6 (without Mentor)
# disci clan * 5 (with Mentor)
# disci off clan * 7 (with Mentor)
def checkXP(character, characterProperties):
    # Get the current XPs for a character
    characterXP = getXPforCharacter(character)

    # Atomic because we can rollback if a player spent more xp than are available
    try:
        with transaction.atomic():
            for property in characterProperties:
                oldValue = property.value
                xPCost = 0

                xPCost = xPCost + ((oldValue + 1) * property.property.type.xpmultiplier)

                if characterXP < xPCost:
                    raise ValueError()

                xpSpentEntry = Xpspent(character=character, oldvalue=oldValue, newvalue=(oldValue + 1),
                                       xpcost=xPCost, property=property.property)
                xpSpentEntry.save()

            return True

    except ValueError:

        return False


# Returns the current spendable XP of a character
def getXPforCharacter(character):
    xpearned = Xpearned.objects.filter(character=character).aggregate(Sum('value'))['value__sum']
    xpspent = Xpspent.objects.filter(character=character).aggregate(Sum('xpcost'))['xpcost__sum']

    if xpearned == None:
        xpearned = 0

    if xpspent == None:
        xpspent = 0

    return xpearned - xpspent


# Gives a random String with length
# used in creating a boon for security reasons
def random_string(length=20):
    pool = string.ascii_letters + string.digits
    return str(''.join(random.choice(pool) for i in range(length)))
