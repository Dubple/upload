from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

import datetime

# Create your models here.

class Folder(models.Model):
    owner = models.ForeignKey(to=User, null=True, blank=True)
    parent = models.ForeignKey(to='self', null=True, blank=True)
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name

class File(models.Model):
    file_id = models.CharField(max_length=25)
    owner = models.ForeignKey(to=User)
    shared = models.ManyToManyField(to=User, blank=True, related_name='shared')
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    date_time = models.DateTimeField(auto_now=False, default=datetime.datetime(2016, 10, 10, 10, 10, 10, 0))
    ip_address = models.GenericIPAddressField(default='0.0.0.0', protocol='IPv4')
    file = models.FileField(upload_to='uploads/%Y/%m/%d')
    folder = models.ForeignKey(to=Folder, null=True, blank=True)

    def __unicode__(self):
        return self.file_id
