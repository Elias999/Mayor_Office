from django.contrib import admin
from django import forms
from .models import complain, infrastructure, crew

class complainAdminForm(forms.ModelForm):

    class Meta:
        model = complain
        fields = '__all__'


class complainAdmin(admin.ModelAdmin):
    form = complainAdminForm
    list_display = ['slug', 'made_afm', 'created', 'resolved', 'infrastructure_id', 'notes', 'resolve_date']
    readonly_fields = ['slug', 'made_afm', 'created',  ]

admin.site.register(complain, complainAdmin)


class infrastructureAdminForm(forms.ModelForm):

    class Meta:
        model = infrastructure
        fields = '__all__'


class infrastructureAdmin(admin.ModelAdmin):
    form = infrastructureAdminForm
    list_display = ['UUID', 'created', 'last_updated', 'google_location', 'type']
    readonly_fields = ['UUID', 'created', 'last_updated']

admin.site.register(infrastructure, infrastructureAdmin)


class crewAdminForm(forms.ModelForm):

    class Meta:
        model = crew
        fields = '__all__'


class crewAdmin(admin.ModelAdmin):
    form = crewAdminForm
    list_display = ['name', 'UUID', 'created', 'last_updated', 'working_hours', 'crew_members', 'complains_id']
    readonly_fields = [ 'UUID', 'created', 'last_updated']

admin.site.register(crew, crewAdmin)
