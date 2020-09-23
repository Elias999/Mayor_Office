# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import date

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app import Populate
from app.models import personel , complain , crew , task , infrastructure
from .forms import NewCrew , NewTask
from django.core import serializers


@login_required(login_url="/login/")
def index(request):
    context = {}
    populating = Populate.Populate("index")
    taskform = NewTask(request.POST or None)

    if 'newtask' in request.POST:
        if taskform.is_valid():
            title = taskform.cleaned_data.get("title")
            text = taskform.cleaned_data.get("text")
        try:
            task.objects.create(title = title, text = text )
            msgproblem = 'New Task added'
        except Exception as e:
                msgproblem = 'No task added' + e
    else:
        msgproblem = 'No task added'
    # data send it
    lastweekdays = populating.lastweek().get('days')
    lastweek = populating.lastweek().get('count')
    sumlastweek = populating.lastweek().get('sum')
    total = populating.count_incid()
    resolved = populating.lastweek_resolved().get('count')
    sumresolved = populating.lastweek_resolved().get('sum')
    un_complain_table = complain.objects.filter(resolved=False)
    task_table = task.objects.all()

    context = {"lastweek" : lastweek , "lastdays" : lastweekdays , "total" : total, "resolved" : resolved , "unresolved" : un_complain_table , "task_table" : task_table , "NewTask" : taskform , "sumlastweek" : sumlastweek , "sumresolved" : sumresolved}
    return render(request, "index.html" ,context)

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
            48
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
        elif "crew_add.html" in request.path:
            complain_table = complain.objects.filter(resolved=False)
            personel_table = personel.objects.all()
            context = { "comptable" : complain_table , "crewform" : crewform ,"msgproblem" : msgproblem, "pertable" : personel_table }
        elif "ui-maps.html" in request.path:
            infrastructure_table = infrastructure.objects.all()
            data = serializers.serialize("json", infrastructure_table , ensure_ascii=False , fields=('google_location','type' ) )
            context = { "infrastructure" : data , "infrastructure_table" : infrastructure_table }


        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except Exception as e:

        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(e)

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



@login_required(login_url="/login/")
def delete(request):

    if "task" in request.GET:
        context = {}
        task.objects.filter(id = request.GET.get('task', '')).delete()
        return  redirect('/')
    else:
        context = {}
        crew.objects.filter(UUID = request.GET.get('crew', '')).delete()
        return  redirect('/ui-tables.html')

def api(request):
    send = {}
    count = []
    days = []
    today_date = date.today()
    for i in range(1,8):
        forming = today_date.day - i
        forming = str(forming) + '/' + str(today_date.month)
        days.append( forming )
    return HttpResponse(str(days))
