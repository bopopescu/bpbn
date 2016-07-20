from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from .models import Character, Person, CharacterProperty, CharacterDiscipline, Clan, Vampire
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return HttpResponse("A beast I am, lest a beast I become!")


@login_required()
def characters(request):
    clans = Clan.objects.all().order_by('name')
    characters = Character.objects.all().order_by('clan')
    context = {'clans': clans, 'characters': characters,}

    return render(request, 'domainmanager/characters.html', context)


@login_required()
def players(request):

    users = User.objects.all()

    #players = Person.objects.all().order_by('lastname')
    characters = Character.objects.all()
    context = {'users': users, 'characters': characters,}

    return render(request, 'domainmanager/players.html', context)


@login_required()
def charactersheet(request, character_id):

    character = get_object_or_404(Character, pk=character_id)

    characterProperties = get_list_or_404(CharacterProperty, character=character)

    cleanProperties = {}

    # Add all character properties into a "clean" dict, so it can be accessed more easily
    for cproperty in characterProperties:
        cleanProperties[cproperty.property.name.replace(" ", "_")] = str(cproperty.value)
        # print("NAME: " + cproperty.property.name + ", VALUE: ", str(cproperty.value))

    # Add all character disciplines into a "clean" dict, so it can be accessed more easily
    characterDisciplines = CharacterDiscipline.objects.all().filter(character=character).order_by('-level')

    cleanDisciplines = {}

    for cdiscipline in characterDisciplines:
        cleanDisciplines[cdiscipline.discipline.name] = cdiscipline.level
        #print("NAME: " + cdiscipline.discipline.name + ", VALUE: ", str(cdiscipline.level))

    context = {'character': character, 'cleanProperties': cleanProperties, 'cleanDisciplines': cleanDisciplines}

    return render(request, 'domainmanager/charactersheet.html', context)


@login_required()
def playersummary(request, player_id):
    player = get_object_or_404(Person, pk=player_id)

    characters = Character.objects.all().filter(pk=player_id)

    context = {'player': player, 'characters': characters}

    return render(request, 'domainmanager/playersummary.html', context)


@login_required()
def genealogy(request):

    vampires = Vampire.objects.all().filter(generation__lte="6").order_by('pk')

    context = {'vampires': vampires}

    return render(request, 'domainmanager/genealogy.html', context)

@login_required()
def createCharacter(request):
    return HttpResponse('Have fun')
