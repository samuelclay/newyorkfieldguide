from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from posts import views as posts_views


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', posts_views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', posts_views.post_detail, name='post-detail'),
    
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
         { 'document_root' : settings.MEDIA_ROOT, 'show_indexes' : False })
    )
