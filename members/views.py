from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members, Comments
from django.urls import reverse

# Create your views here.
def index(request):
	mymembers = Members.objects.all().values()
	comments = Comments.objects.all().values()
	template = loader.get_template("index.html")
	context = {
		"mymembers": mymembers,
		"comments":comments
	}
	return HttpResponse(template.render(context, request))

def add(request):
	template = loader.get_template("add.html")
	return HttpResponse(template.render({},request))

def addrecord(request):
	x = request.POST["first"]
	y = request.POST["last"]
	member = Members(firstname=x, lastname=y)
	member.save()
	return HttpResponseRedirect(reverse("index"))

def delete(request, id):
	member = Members.objects.get(id=id)
	member.delete()
	return HttpResponseRedirect(reverse("index"))

def update(request, id):
	template = loader.get_template("update.html")
	member = Members.objects.get(id=id)
	context = {
		"member":member
	}
	return HttpResponse(template.render(context,request))

def updaterecord(request, id):
	firstname = request.POST["first"]
	lastname = request.POST["last"]
	member = Members.objects.get(id=id)
	member.firstname = firstname
	member.lastname = lastname
	member.save()
	return HttpResponseRedirect(reverse("index"))

def addcomment(request):
	template = loader.get_template("addcomment.html")
	return HttpResponse(template.render({},request))

def submitcomment(request):
	name = request.POST["name"]
	text = request.POST["text"]
	comment = Comments(name=name, text=text)
	comment.save()
	return HttpResponseRedirect(reverse("index"))

def deletecomment(request, id):
	toDelete = Comments.objects.get(id=id)
	toDelete.delete()
	return HttpResponseRedirect(reverse("index"))

def cv(request):
	template = loader.get_template("cv.html")
	return HttpResponse(template.render({},request))