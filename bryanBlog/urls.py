from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'bryanBlog.views.home', name='home'),
    url(r'^$', include('zinnia.urls')),
    # url(r'^bryanBlog/', include('bryanBlog.foo.urls')),
	url(r'^weblog/', include('zinnia.urls')),
	url(r'^comments/', include('django.contrib.comments.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
