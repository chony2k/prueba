from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap
from  mysite.views import  word_count



admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
    #    {'sitemaps': {'cmspages': CMSSitemap}}),
    #url(r'^', include('cms.urls')),
    url(r'^mysite/wordcount', word_count, name="word_count")
)
