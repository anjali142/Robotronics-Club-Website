from django.shortcuts import render

from .models import Member, Project, Tutorial

def index(request):
    return render(request, 'robotronics/index.html')

def about(request):
    return render(request, 'robotronics/about.html')

def team(request):
    faculty = Member.objects.filter(role='Faculty')
    coord = Member.objects.filter(role='Coord')
    team = Member.objects.filter(role='Team')
    webdev = Member.objects.filter(role='WebDev'),
    return render(request, 'robotronics/team.html', {
        'faculty': faculty,
        'coord': coord,
        'team': team,
        'webdev': webdev,
    })

def contacts(request):
    return render(request, 'robotronics/contacts.html')

def tutorial(request):
    list_tutorials = Tutorial.objects.all()
    return render(request, 'robotronics/tutorial.html', {'list_tutorials': list_tutorials})

def project(request):
    list_projects = Project.objects.all()
    return render(request, 'robotronics/project.html', {'list_projects': list_projects})
