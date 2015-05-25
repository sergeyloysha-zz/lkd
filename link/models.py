# coding:utf-8
from urlparse import urlparse
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import tweepy
import vkontakte

vk_token = '7e9e2a55d16bf6dfa17ab002ea9d63c99e281f8c983a569a699b0ad04023407e6c6d1760f26ca12400492'

# Create your models here.

class Link(models.Model):
    class Meta():
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    link_title = models.CharField(max_length=250)
    link_slug = models.SlugField(max_length=250)
    link_url = models.URLField()
    link_category = models.ForeignKey('link.Category', default=lambda: Category.objects.get(id=1))
    link_author = models.ForeignKey(User, default=1)
    link_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.link_title

    @property
    def domain(self):
        return urlparse(self.link_url).netloc

    @permalink
    def get_absolute_url(self):
        return ('view_link', None, { 'id': self.id })

    @permalink
    def get_redirect_url(self):
        return ('redirect_link', None, { 'id': self.id })

    def save(self, *args, **kwargs):

        self.link_slug = slugify(self.link_title.encode(settings.DEFAULT_CHARSET))

        super(Link, self).save(*args, **kwargs)

        if settings.VK_ON:
            try:
                vk = vkontakte.API(token=settings.VK_APP_TOKEN)
                vk.wall.post(owner_id=settings.VK_APP_PUBLIC, message="%s \n\n #%s@lkdto \n\n %s" % (self.link_title, str(self.link_category).lower(), self.link_url))
            except:
                pass

        if settings.TWITTER_CONSUMER_KEY and settings.TWITTER_ON:
            try:
                auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
                auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)

                api = tweepy.API(auth)
                api.update_status("%s %s #%s" % (self.link_title[0:110], self.link_url, str(self.link_category).lower()))
            except:
                pass

    
class Category(models.Model):
    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    category_title = models.CharField(max_length=250)
    category_slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.category_title

    @permalink
    def get_absolute_url(self):
        return ('view_link_category', None, { 'slug': self.category_slug })