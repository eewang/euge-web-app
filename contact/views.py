from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import RequestContext
from contact.forms import ContactListForm
from contact.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def contact_list(request):
	all_contacts = Contact.objects.all().order_by('last_name')
	paginator = Paginator(all_contacts, 3)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render_to_response('contact_page.html', context_instance=RequestContext(request, {"contacts": contacts}))

def contact_list_add(request):
	if request.method == 'POST':
		form = ContactListForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contact_list/save/')
	else:
		form = ContactListForm()
	return render_to_response('contact_list_add.html', {'form': form}, context_instance=RequestContext(request))

def contact_list_save(request):
	return render_to_response('contact_list_save.html', context_instance=RequestContext(request))
