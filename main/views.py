from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial

# Create your views here.
def homepage(request):
	#return HttpResponse("WOW this is <strong>html</strong>")
	return render(request=request,
				  template_name="main/home.html",
				  context={"tutorials":Tutorial.objects.all}) # refers to tutorial template
	# filepath = main/templates/main/home.html