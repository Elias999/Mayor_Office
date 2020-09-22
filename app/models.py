from django.db import models as models
from django.contrib.auth import models as auth_models
from django_extensions.db import fields as extension_fields
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import BooleanField
from django.db.models import AutoField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.db.models import UUIDField
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
import uuid
from autoslug import AutoSlugField

class complain(models.Model):

    # Fields
    slug = models.AutoField(primary_key=True)
    slug_ref = AutoSlugField(populate_from="slug")
    made_afm = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    resolved = models.BooleanField(default='False')
    infrastructure_id = models.ForeignKey("infrastructure", on_delete=models.CASCADE)
    notes = models.TextField(max_length=300)
    resolve_date = models.DateTimeField(blank = True,null = True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_complain_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_complain_update', args=(self.slug,))


class infrastructure(models.Model):

    # Fields
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    google_location = models.CharField(max_length=30)
    type = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_infrastructure_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_infrastructure_update', args=(self.pk,))


class crew(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug_ref = AutoSlugField(populate_from="UUID")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    working_hours = models.CharField(max_length=30)
    crew_members = models.TextField(max_length=30)
    complains_id = models.TextField(max_length=330)
    total_assigments = models.CharField(max_length=6)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_crew_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_crew_update', args=(self.pk,))


class personel(models.Model):

    # Fields
    name = models.CharField(max_length=40)
    specialization = models.CharField(max_length=9)
    hired = models.DateTimeField(auto_now_add=True, editable=False)
    salary = models.CharField(max_length=8)



    class Meta:
        ordering = ('-hired',)


    def get_absolute_url(self):
        return reverse('app_personel_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_personel_update', args=(self.slug,))

class task(models.Model):

    # Fields
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=200)
    done = models.BooleanField(default='False')


    class Meta:
        ordering = ('-done',)


    def get_absolute_url(self):
        return reverse('app_task_title', args=(self.slug,))


    def get_update_url(self):
        return reverse('app_task_title', args=(self.slug,))
