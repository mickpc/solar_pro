from django.conf.urls import patterns, include, url

from django.contrib import admin
from graph3 import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sol3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^graph/$', views.graph, name="graph"),

)