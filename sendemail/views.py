from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['first']
            last = form.cleaned_data['last']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(first + ' ' + last, message, from_email, ['robotronics@iitmandi.ac.in'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contacts')
    return render(request, "robotronics/contacts.html", {'form': form})
