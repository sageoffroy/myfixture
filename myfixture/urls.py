from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fixture.views.user_login'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^selecciones.*/$','fixture.views.selecciones'),
    url(r'^fixture.*/$','fixture.views.fixture'),
    url(r'^contacto.*/$','fixture.views.contacto'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.*/', 'fixture.views.user_login'),
    url(r'^logout/$', 'fixture.views.user_logout'),
    url(r'^register/$','fixture.views.user_register'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	url(r'^css/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.CSS_ROOT,}
	),
)
