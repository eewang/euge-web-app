from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from vocab.forms import *
from django.template import RequestContext
from vocab.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def vocab_list(request):
	all_vocab = Vocab.objects.all().order_by('word')
	paginator = Paginator(all_vocab, 5)
	page = request.GET.get('page')
	try:
		vocab = paginator.page(page)
	except PageNotAnInteger:
		vocab = paginator.page(1)
	except EmptyPage:
		vocab = paginator.page(paginator.num_pages)
	return render_to_response('vocab_page.html', context_instance=RequestContext(request, {'vocab': vocab})) 

def vocab_list_add(request):
	if request.method == 'POST':
		form = VocabListForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpReponseRedirect('/vocab/save/')
	else:
		form = VocabListForm()
	return render_to_response('vocab_list_add.html', {'form': form}, context_instance=RequestContext(request))

def vocab_list_save(request):	
	return render_to_response('vocab_list_save.html', context_instance=RequestContext(request))
