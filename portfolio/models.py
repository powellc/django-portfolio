from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from tagging.fields import TagField
from portfolio.managers import PublicManager

import tagging

class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    
    class Meta:
        db_table = "clients"
        ordering = ['name']
        
    def __unicode__(self):
        return self.name
    
class Medium(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    
    class Meta:
        db_table = "media"
        verbose_name_plural = "media"
        ordering = ['name']
    
    def __unicode__(self):
        return self.name
        
    @permalink
    def get_absolute_url(self):
        return self.slug
    
class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    project_url = models.URLField('Project URL')
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client)
    media = models.ManyToManyField(Medium)
    disciplines = TagField()
    completion_date = models.DateField()
    in_development = models.BooleanField()
    is_public = models.BooleanField(default=True)
    overview_image = models.ImageField(upload_to="projects/overview/")
    detail_image = models.ImageField(upload_to="projects/detail/")
    objects         = PublicManager()
    
    class Meta:
        db_table = "projects"
        ordering = ['-completion_date']
        
    def __unicode__(self):
        return self.name
    
    @permalink
    def get_absolute_url(self):
        return self.slug