from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect

from . import forms
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

def proj(request, project_id):
    proj = get_object_or_404(Project, id=project_id)
    previousp = Project.objects.filter(id__lt=project_id).last()
    nextp = Project.objects.filter(id__gt=project_id).first()
    return render(request, 'robotronics/postP.html', {'proj': proj, 'previousp': previousp, 'nextp': nextp})

def tut(request, tutorial_id):
    tut = get_object_or_404(Tutorial, id=tutorial_id)
    previousp = Tutorial.objects.filter(id__lt=tutorial_id).last()
    nextp = Tutorial.objects.filter(id__gt=tutorial_id).first()
    return render(request, 'robotronics/postT.html', {'tut': tut, 'previousp': previousp, 'nextp': nextp})

def send_mail(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['varunjustrocks@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
