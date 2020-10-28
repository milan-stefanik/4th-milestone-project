from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ A view to return the index page """

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            messageData = {
                'first_name': form.cleaned_data['first_name'].title,
                'last_name': form.cleaned_data['last_name'].title,
                'email': form.cleaned_data['email'],
                'phone':  form.cleaned_data['phone'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
                'companyEmail': settings.DEFAULT_FROM_EMAIL,
            }

            subject = render_to_string(
                'home/emails/subject.txt',
                {'messageData': messageData})
            body = render_to_string(
                'home/emails/body.txt',
                {'messageData': messageData})

            send_mail(
                subject,
                body,
                messageData['email'],
                [messageData['companyEmail']]
            )

            if form.cleaned_data['send_copy']:
                subject = render_to_string(
                    'home/emails/subject-copy.txt',
                    {'messageData': messageData})
                body = render_to_string(
                    'home/emails/body-copy.txt',
                    {'messageData': messageData})

                send_mail(
                    subject,
                    body,
                    messageData['companyEmail'],
                    [messageData['email']]
                )

            context = {
                'api_key': settings.GOOGLE_MAPS_API_KEY,
                'form': form,
            }
            messages.success(request, 'Your message has been sent. \
            We will contact you soon.')
            return redirect('contact')

    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY,
        'form': form,
    }
    return render(request, 'home/contact.html', context)
