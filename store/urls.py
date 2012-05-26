from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from products.models import *
from django.views.generic import list_detail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.list_detail',
    # Examples:
    # url(r'^$', 'store.views.home', name='home'),
    # url(r'^store/', include('store.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^grappelli/', include('grappelli.urls')),
     url(r'^admin/', include(admin.site.urls)),
        url(r'^product/$', 'object_list', {'queryset': Product.objects.all()}),
        url(r'^product/(?P<slug>[-\w]+)/$', 'object_detail', {'queryset': Product.objects.all()}),
)
