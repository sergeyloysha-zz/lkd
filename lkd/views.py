from link.models import Link, Category
from link.forms import LinkForm
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from django.core.context_processors import csrf
from django.conf import settings
from django.contrib import auth
import datetime

from django.contrib.auth.decorators import login_required

def index(request):
	links_list = Link.objects.all().order_by('-link_created')
	paginator = Paginator(links_list, 10)

	page = request.GET.get('page')

	try:
		links = paginator.page(page)
	except PageNotAnInteger:
		links = paginator.page(1)
	except EmptyPage:
		links = paginator.page(paginator.num_pages)

	return render(request, 'index.html', {
		'categories': Category.objects.all(),
		'links': links,#.filter(link_category=3)
	})

@login_required
def new(request):

	c = {}
	c.update(csrf(request))

	if request.method == "POST":
		c['form'] = LinkForm(request.POST)
		if c['form'].is_valid():
			link = c['form'].save(commit=False)
			link.link_author = request.user
			link.save()
			return HttpResponseRedirect("/")
	else:
		c['form'] = LinkForm()

	return render(request, 'new.html', {
		'form': c['form']
	})