from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def resume_content(request):
	return render_to_response('resume_content.html', context_instance=RequestContext(request))

