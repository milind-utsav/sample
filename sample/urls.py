from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'sample.views.response'),
    url(r'^admin/', include(admin.site.urls)),
)
