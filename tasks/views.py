from django.shortcuts import render_to_response
from tasks.models import List, Item
from django.template import RequestContext

def tasks_list(request):
	task_listing = []
	for task_list in List.objects.all():
		task_dict = {}
		task_dict['list_object'] = task_list
		task_dict['item_count'] = task_list.item_set.count()
		task_dict['items_complete'] = task_list.item_set.filter(completed=True).count()
		task_dict['percent_complete'] = int(float(task_dict['items_complete']) / task_dict['item_count']*100)
		task_listing.append(task_dict)
	return render_to_response('tasks_list.html', context_instance=RequestContext(request, {
		'task_listing': task_listing,
	}))

