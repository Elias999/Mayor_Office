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
import math
from numpy import linalg

#from app.Populate import *


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
    perMonthCosts = populating.perMonthCosts()
    perTypeIncidents = populating.perTypeIncidents()
    perTypeFailPos = populating.perTypeFailPos()
    perMonthIncidents = populating.perMonthIncidents()

    context = {"lastweek" : lastweek ,
     "lastdays" : lastweekdays ,
     "total" : total,
      "resolved" : resolved ,
       "unresolved" : un_complain_table ,
      "task_table" : task_table ,
       "NewTask" : taskform ,
        "sumlastweek" : sumlastweek ,
       "sumresolved" : sumresolved,
        "perMonthCosts" : perMonthCosts ,
        "perTypeIncidents" : perTypeIncidents,
         "perTypeFailPos" : perTypeFailPos,
         "perMonthIncidents" : perMonthIncidents}
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
        elif "ui-notifications.html" in request.path:
            populating = Populate.Populate("index")
            perTypeAlerts1 = populating.perTypeAlerts1()
            perTypeAlerts2 = populating.perTypeAlerts2()
            perTypeAlerts3 = populating.perTypeAlerts3()
            perTypeAlerts4 = populating.perTypeAlerts4()
            perTypeAlerts5 = populating.perTypeAlerts5()
            perTypeAlerts6 = populating.perTypeAlerts6()
            curMonthIncidents = populating.curMonthIncidents()
            curMonthType = populating.curMonthType()
            curMonthCost = populating.curMonthCost()
            successfulRepairs = populating.successfulRepairs()
            context = {"perTypeAlerts1" : perTypeAlerts1 ,
            "perTypeAlerts2" : perTypeAlerts2 ,
            "perTypeAlerts3" : perTypeAlerts3 ,
            "perTypeAlerts4" : perTypeAlerts4 ,
            "perTypeAlerts5" : perTypeAlerts5 ,
            "perTypeAlerts6" : perTypeAlerts6 ,
             "curMonthIncidents" : curMonthIncidents ,
             "curMonthType" : curMonthType,
              "curMonthCost" : curMonthCost,
              "successfulRepairs": successfulRepairs}
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


def crewLogin(theuuid):
    theuuid.replace(' ','')
    crewUUID = list(crew.objects.all())
    finalUUID = 'crew object (' + theuuid + ')'
    #return HttpResponse(str(crewUUID))
    if str(finalUUID) in str(crewUUID):
        return True
    else:
        return False



def euclidianDistance(x1,x2,y1,y2):
    x = float(sqrt((float(x2)-float(x1)) + (float(y2)-float(y1))**2))
    return x


def smartPath():
    firstTime = True
    allComplains = complain.objects.all().filter(resolved = False)
    google_locations = []
    startX, startY = 37.9415179, 23.6506794
    counter = 0
    for entry in allComplains:
        counter += 1
        infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
        findinf = infrastructure.objects.all().filter(UUID = infID)
        type = ''
        for result in findinf:
            type = str(result.google_location).split(',')
            google_locations.append([float(type[0]),float(type[1])])
    answer = float(10000000000000000000000.0)
    answerX, answerY = 0.0, 0.0
    done = []
    for k in range(counter):
        answer = float(10000000000000000000000.0)
        for coords in google_locations:
            if([coords[0], coords[1]] not in done):
                x = math.pow(startX + float(coords[0]) , 2)
                y = math.pow(startY + float(coords[1]) , 2)
                final = math.pow(x+y , 0.5)
                if final < answer:
                    answer = final
                    answerX, answerY = coords[0], coords[1]
        done.append([startX, startY])
        google_locations.remove([answerX, answerY])
        startX, startY = float(answerX), float(answerY)
    done.append([startX, startY])
    bigString = ''
    i = 1
    for coords in done:
        if firstTime:
            bigString += "You are at " + str(coords) + "\n"
            firstTime = False
        else:
            bigString += "Stop No " + str(i) + " at " + str(coords) + "\n"
            i += 1
    for entry in allComplains:
        entry.resolved = True
        entry.save()
    return bigString



def givePreviousComplains(userAFM):
    userComplains = complain.objects.all().filter(made_afm = userAFM)
    answer = ""
    complainResolved= ''
    counter = 0
    for entry in userComplains:
        counter += 1
        if entry.resolved == True:
            complainResolved = 'Yes'
        else:
            complainResolved = 'False'
        answer += "Complain No " + str(entry.slug) + "\nMade in " + str(entry.created) + "\nNoted:  " + str(entry.notes) + "\nResolved:  " + complainResolved + "\n\n"
    if counter > 0:
        return str(answer)
    else:
        return "No complains found with given AFM!"

def returnOptions():
    toreturn = infrastructure.objects.all()
    answer = []
    for entry in toreturn:
        answer.append(entry.UUID)
        answer.append(',')
    return answer

def dbOnCreateResponse(afm, infID, dmgtype):
    infrIdent = 'infrastructure object (' + infID + ')'
    infr = infrastructure.objects.all().filter(UUID = infID)
    for entry in infr:
        infID = entry

    try:
        complain.objects.create(made_afm = afm, infrastructure_id = infID, notes = dmgtype)
        return 'New complain added'
    except Exception as e:
        return e


def api(request):
    if request.method == 'GET':
        type = request.GET.get('action')
        #arg = request.GET.get('uuid', '')
        if type == 'login':
            theuuid = request.GET.get('uuid')
            if crewLogin(theuuid):
                return HttpResponse("crew")
            else:
                return HttpResponse("notACrew")
        elif type == 'ontofix':
            return HttpResponse(str(smartPath()))
        elif type == 'previous':
            userAFM = request.GET.get('afm')
            return HttpResponse(str(givePreviousComplains(userAFM)))
        elif type == 'icomplain':
            afm = request.GET.get('afm')
            infID = request.GET.get('infID')
            dmgtype = request.GET.get('type')
            return HttpResponse(str(dbOnCreateResponse(afm, infID, dmgtype)))
        elif type == 'givemeoptions':
            return HttpResponse(returnOptions())
