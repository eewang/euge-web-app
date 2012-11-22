from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('polls.views',
	url(r'^polls/$', 'index'),
	url(r'^polls/(?P<poll_id>\d+)/$', 'details'),
	url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
	url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
)

urlpatterns += patterns('',
	url(r'^admin/doc/', include(admin.site.urls)),
	url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('blog.views',
	url(r'^$', 'home'),
	url(r'^blog/$', 'index'),
	url(r'^blog/create/$', 'blog_post'),
	url(r'^test/$', 'current'),
	url(r'^test2/$', 'display_meta'),
	url(r'^search/$', 'search'),
	url(r'^contact/$', 'contact'),
#	url(r'^posts/(?P<y>\d{4})/$', 'year_archive')
	url(r'^eugene/$', 'eugene_archive'),

#	Generic Views
	url(r'^links/$', direct_to_template, {
		'template': 'links.html'
	}),	
	url(r'^blog/save/$', direct_to_template, {
		'template': 'blog_form_save.html'
	}),

)

urlpatterns += patterns('contact.views',
	url(r'^contact_list/$', 'contact_list'),
	url(r'^contact_list/add/$', 'contact_list_add'),
	url(r'^contact_list/save/$', 'contact_list_save'),
)

urlpatterns += patterns('vocab.views',
	url(r'^vocab/$', 'vocab_list'),
	url(r'^vocab/add/$', 'vocab_list_add'),
	url(r'^vocab/save/$', 'vocab_list_save'),
)

urlpatterns += patterns('maps.views',
	url(r'^maps/nyc_electric/$', 'nyc_electric'),
)

urlpatterns += patterns('tasks.views',
	url(r'^tasks/$', 'tasks_list'),
)

urlpatterns += patterns('resume.views',
	url(r'^resume/$', 'resume_content'),
)

urlpatterns += patterns('walkman.views',
	url(r'^walkman/draganddrop/$', 'draganddrop'), 
)
