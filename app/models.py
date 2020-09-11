from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.db.models import UUIDField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
import uuid

class complain(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='id',max_length=255,unique=True)
    made_afm = models.CharField(max_length=9)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    resolved = models.BooleanField(default='False')
    infrastructure_id = models.ForeignKey("infrastructure", on_delete=models.CASCADE)
    notes = models.TextField(max_length=300)
    resolve_date = models.DateTimeField()


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
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    working_hours = models.CharField(max_length=30)
    crew_members = models.TextField(max_length=30)
    complains_id = models.TextField(max_length=330)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('app_crew_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('app_crew_update', args=(self.pk,))
