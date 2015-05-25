# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import hashlib
from django.db.models import permalink
 
 
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    post = models.CharField(max_length=250, verbose_name='Должность', blank=True)

    @permalink
    def get_absolute_url(self):
        return ('view_user', None, { 'id': self.user.id })

    def gravatar_url(self):
		return "http://www.gravatar.com/avatar/%s?s=100" % hashlib.md5(self.user.email).hexdigest()
 
    def __unicode__(self):
        return unicode(self.user)
 
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'