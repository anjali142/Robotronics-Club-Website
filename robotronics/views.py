from django.shortcuts import render

from .models import Member, Project, Tutorial

def index(request):
    return render(request, 'robotronics/index.html')

def about(request):
    return render(request, 'robotronics/about.html')

def team(request):
    coord16 = Member.objects.filter(role='Coord16')
    coord = Member.objects.filter(role='Coord')
    team = Member.objects.filter(role='Team')
    team16 = Member.objects.filter(role='Team16')
    return render(request, 'robotronics/team.html', {
        'coord16': coord16,
        'coord': coord,
        'team': team,
        'team16': team16,
    })

def contacts(request):
    return render(request, 'robotronics/contacts.html')

def tutorial(request):
    list_tutorials = Tutorial.objects.all()
    return render(request, 'robotronics/tutorial.html', {'list_tutorials': list_tutorials})

def project(request):
    list_projects = Project.objects.all()
    return render(request, 'robotronics/project.html', {'list_projects': list_projects})
