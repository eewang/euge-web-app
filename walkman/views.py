from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def draganddrop(request):
	return render_to_response('DragAndDrop.html', context_instance=RequestContext(request))

