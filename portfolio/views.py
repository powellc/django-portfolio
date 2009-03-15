from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from django.views.generic import date_based, list_detail
from portfolio.models import Project, Medium

def project_list(request, page=0, **kwargs):
    return list_detail.object_list(
        request,
        queryset=Project.objects.public(),
        paginate_by=5,
        page=page,
        **kwargs
    )
project_list.__doc__ = list_detail.object_list.__doc__

def medium_list(request, **kwargs):
    return list_detail.object_list(
        request,
        queryset = Medium.objects.all(),
        **kwargs
    )
