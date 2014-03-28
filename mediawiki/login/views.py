from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	return render_to_response('login/home.html', {}, context_instance=RequestContext(request))

def signin(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/%s/' % request.user.username) 
		else:
			return HttpResponse("Your account is disabled!")
	else:
		return HttpResponse("your username or password is incorrect!")

def signup(request):
	if request.POST:
		user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
		#u=user.userprofile_set.create()
		user.save()
		return render_to_response('login/successfullSignup.html', context_instance=RequestContext(request))	
	else:
		return render_to_response('login/signup.html', context_instance=RequestContext(request))

def signout(request):
	logout(request)
	return render_to_response('login/signout.html', context_instance=RequestContext(request))
