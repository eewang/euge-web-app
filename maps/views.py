from django.shortcuts import render_to_response
from django.http import HttpResponse

def nyc_electric(request):
	return HttpResponse('maps/layers/index.html', request)

