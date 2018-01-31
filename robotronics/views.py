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

def emailView(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "robotronics/contacts.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
