from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from posts import views as posts_views


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', posts_views.index, name='index'),
    url(r'^photo/(?P<slug>[\w-]+)(?P<year>[\d-]+)(?P<day>[\d-]+)(?P<month>[\d-]+)/$', posts_views.photo_detail, name='photo_detail'),
    url(r'^(?P<slug>[\w-]+)/$', posts_views.post_detail, name='post-detail'),
    
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^m/(?P<path>.*)$', 'django.views.static.serve', 
         { 'document_root' : settings.MEDIA_ROOT, 'show_indexes' : False })
    )