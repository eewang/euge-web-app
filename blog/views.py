from django.shortcuts import render_to_response
from blog.models import Post, Author
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from blog.forms import ContactForm, BlogForm

def home(request):
	return render_to_response('home_body.html', context_instance=RequestContext(request))

def blog(request):
	all_posts = Post.objects.all().order_by('-date')
	template_data = {'posts' : all_posts}

	return render_to_response('blog.html', context_instance=RequestContext(request, template_data))

def current(request):
	return HttpResponse("Welcome to the test page at %s" % request.path)

def display_meta(request):
	values = request.META.items()
	values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q)>20:
			errors.append('Please enter no more than 20 characters')
		else:
			posts = Post.objects.filter(title__icontains=q)
			return render_to_response('search_results.html', {'posts': posts, 'query': q})
	return render_to_response('search_form.html', {'errors': errors})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'I love your blog!'}
		)
	return render_to_response('contact_form.html', context_instance=RequestContext(request, {'form': form}))

def year_archive(request, y):
	return Post.objects.filter(Post__date__year=y)

def eugene_archive(request):
	return HttpResponse(Post.objects)

def blog_post(request):
	if request.method == 'POST':
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blog/save/')
	else:
		form = BlogForm()
	return render_to_response('blog_form.html', {'form': form}, context_instance=RequestContext(request))

