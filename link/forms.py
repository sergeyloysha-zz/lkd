# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from link.models import Link

class LinkForm(ModelForm):
	class Meta:
		model = Link
		exclude = ('link_slug','link_author',)
		widgets = {
			'link_title': forms.TextInput(attrs={'placeholder':u'Заголовок'}),
			'link_url': forms.TextInput(attrs={'placeholder':u'Ссылка на материал'}),
			'link_category': forms.RadioSelect(),
		}