from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from people.models import Name, Country, Email, User_email, User_name, User_country

def home(request, username):
	user = request.user
	if username == user.username:
		if request.POST:
			user.username = request.POST['username']
			user.first_name = request.POST['firstname']
			user.last_name = request.POST['lastname']
			user.email = request.POST['email']
			user.save()
		name_id = User_name.objects.filter(user_id = user.id)
		user.identifiers_name = Name.objects.filter(id__in = (i.name_id for i in name_id))
		country_id = User_country.objects.filter(user_id = user.id)
		user.identifiers_country = Country.objects.filter(id__in = (i.country_id for i in country_id))
		email_id = User_email.objects.filter(user_id = user.id)
		user.identifiers_email = Email.objects.filter(id__in = (i.email_id for i in email_id))
		return render_to_response('people/home.html', {"user":user}, context_instance=RequestContext(request))
	else:
		return HttpResponse("Viewing other' profile feature needs to be implemented...")

def addIdentity(request, username, identifier):
	user = request.user
	user.identifier = identifier
	if username == user.username:
		if request.POST:
			a=request.POST.getlist('id')
			if identifier == 'name':
				for i in a:
					data = user.user_name_set.create(name_id = i)
					data.save()
			if identifier == 'country':
				for i in a:
					data = user.user_country_set.create(country_id = i)
					data.save()
			if identifier == 'email':
				for i in a:
					data = user.user_email_set.create(email_id = i)
					data.save()
		if identifier == 'name':
			identifier_id = User_name.objects.filter(user_id = user.id)
			user.identifiers = Name.objects.filter(id__in = (i.name_id for i in identifier_id))
			user.list = Name.objects.all()[:100]
		elif identifier == 'country':
			identifier_id = User_country.objects.filter(user_id = user.id)
			user.identifiers = Country.objects.filter(id__in = (i.country_id for i in identifier_id))
			user.list = Country.objects.all()[:100]
		elif identifier == 'email':
			identifier_id = User_email.objects.filter(user_id = user.id)
			user.identifiers = Email.objects.filter(id__in = (i.email_id for i in identifier_id))
			user.list = Email.objects.all()[:100]
		return render_to_response("people/add.html", {'identifier':identifier, 'user':user}, context_instance=RequestContext(request))
	else:
		return HttpResponse("You cannot add Identities to others profile...")

def removeIdentity(request, username, identifier, Id):
	user = request.user
	if username != user.username:
		return HttpResponse("Error!")
	if identifier == 'name':
		user.user_name_set.filter(user_id=user.id, name_id=Id).delete()
	elif identifier == 'country':
		user.user_country_set.filter(user_id=user.id, country_id=Id).delete()
	elif identifier == 'email':
		user.user_email_set.filter(user_id=user.id, email_id=Id).delete()
	return HttpResponse("Success")