from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacted
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
		return redirect('/')
	return render(request, 'index.html' )