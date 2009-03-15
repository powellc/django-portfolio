from django.conf.urls.defaults import *
from portfolio import views as portfolio_views

urlpatterns = patterns('',
    url(r'^page/(?P<page>\w)/$',
        view=portfolio_views.project_list,
        name='portfolio_index_paginated'),

    url(r'^$',
        view=portfolio_views.project_list,
        name='portfolio_index'),
)