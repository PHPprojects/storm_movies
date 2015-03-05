from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    # Examples:
    # url(r'^$', 'teste_storm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
