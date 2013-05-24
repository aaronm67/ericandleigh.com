from django.http import HttpResponse
from django.shortcuts import render;

def index(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "index.html", context)
	
def stuff(request, item):
	return HttpResponse(item, content_type = "text/plain")

def photos(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "photos.html", context)

def registry(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "registry.html", context)

def theproposal(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "theproposal.html", context)

def ourstory(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "ourstory.html", context)

def rsvp(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "rsvp.html", context)

def weddingevents(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "weddingevents.html", context)

def weddingparty(request):
    context = { "title" : "Eric and Leigh" }
    return render(request, "weddingparty.html", context)
