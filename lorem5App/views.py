from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacted

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
	if request.method == 'POST':
		contact = Contacted()
		name = request.POST.get('Name')
		email = request.POST.get('Email')
		message = request.POST.get('Message')
		contact.name = name
		contact.email = email
		contact.message = message
		contact.save()
		send_mail('contact form', f'Name: {name}\nEmail: {email}\nMessage: {message}', settings.EMAIL_HOST_USER, ['gunagang24@gmail.com'], fail_silently=False)
		return redirect('/')
	return render(request, 'index.html' )