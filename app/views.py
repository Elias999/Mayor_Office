# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import personel , complain , crew
from .forms import NewCrew

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    msg = None
    msgproblem = None
    crewform = NewCrew(request.POST or None)
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    if 'newcrew' in request.POST:
        if crewform.is_valid():
            name = crewform.cleaned_data.get("name")
            working_hours = crewform.cleaned_data.get("working_hours")
            crew_members = crewform.cleaned_data.get("crew_members")
            complains_id = crewform.cleaned_data.get("complains_id")
            total = complains_id.count(",") + 1
            try:
                crew.objects.create(name = name, working_hours = working_hours, crew_members = crew_members,complains_id=complains_id,total_assigments = total )
                msgproblem = 'New crew added'
            except Exception as e:
                    msgproblem = 'No new crew' + e
        else:
            msgproblem = 'No new crew'
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        if "ui-tables.html" in request.path:
            crew_table = crew.objects.all()
            personel_table = personel.objects.all()
            context = { "table" : personel_table , "crewtable" : crew_table }
        if "crew_add.html" in request.path:
            complain_table = complain.objects.all()
            personel_table = personel.objects.all()
            context = { "comptable" : complain_table , "crewform" : crewform ,"msgproblem" : msgproblem, "pertable" : personel_table }
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

def forms(request):
    try:
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))


def api(request):
    context = {}
    return HttpResponse("Success", content_type='text/plain')
