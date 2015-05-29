from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^thankyou/','signups.views.thankyou', name='thankyou'),
    url(r'^more/','signups.views.more', name='more'),
    #museum
    url(r'^museum/','signups.views.museum',name='museum'),
    url(r'^m(?P<id>\d+)/$','signups.views.detail', name='detail'),
    url(r'^ctag(?P<tag2>\w+)/$','signups.views.search_tag2', name='search_tag2'),
    url(r'^mtag(?P<tag>\w+)/$','signups.views.search_tag', name='search_tag'),
    url(r'^ktag/','signups.views.k_tag', name='ktag'),
    url(r'^xtag/','signups.views.x_tag', name='xtag'),
    #commercial
    url(r'^commercial/','signups.views.commercial',name='commercial'),
    url(r'^c(?P<id>\d+)/$','signups.views.detail2', name='detail2'),
   
    url(r'^ztag/','signups.views.z_tag', name='ztag'),
    url(r'^qtag/','signups.views.q_tag', name='qtag'),    
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)