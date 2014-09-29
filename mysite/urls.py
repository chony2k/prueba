#coding=UTF-8

from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from  mysite.views import *

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mysite/$', index, name="index"),
    url(r'^mysite/index$', index, name="index"),
    url(r'^mysite/phrases_per_date', phrases_per_date, name="phrases_per_date"),
    url(r'^mysite/wordcount', word_count, name="word_count"),
    url(r'^mysite/rotations', rotations, name="rotations"),
)
