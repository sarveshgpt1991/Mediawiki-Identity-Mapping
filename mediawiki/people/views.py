from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request, username):
	u = request.user
	if username == u.username:
		if request.POST:
			u.username = request.POST['username']
			u.first_name = request.POST['firstname']
			u.last_name = request.POST['lastname']
			u.email = request.POST['email']
			u.save()
		return render_to_response('people/home.html', {"user":u}, context_instance=RequestContext(request))
	else:
		return HttpResponse("Viewing other' profile feature needs to be implemented...")