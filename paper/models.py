# coding:utf-8

from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User

# Create your models here.

class Paper(models.Model):
    paper_title = models.CharField(max_length=250, unique=True)
    paper_slug = models.SlugField(max_length=250, unique=True)
    paper_text = models.TextField()
    paper_category = models.ForeignKey('paper.Category')
    paper_created = models.DateTimeField(db_index=True ,auto_now_add=True)
    paper_updated = models.DateTimeField(auto_now=True)
    paper_author = models.ForeignKey(User)

    def __unicode__(self):
        return self.paper_title

    @permalink
    def get_absolute_url(self):
        return ('view_paper', None, { 'slug': self.paper_slug })

class Category(models.Model):
    category_title = models.CharField(max_length=250, db_index=True)
    category_slug = models.SlugField(max_length=250, db_index=True)

    def __unicode__(self):
        return self.category_title

    @permalink
    def get_absolute_url(self):
        return ('view_paper_category', None, { 'slug': self.category_slug })

class Comment(models.Model):
    comment_text = models.TextField()
    comment_paper = models.ForeignKey('paper.Paper')
    comment_author = models.ForeignKey(User)
    comment_created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.comment_text