from link.models import Link, Category
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse

def view_link_category(request, slug):

	category = get_object_or_404(Category, category_slug=slug)

	links_list = Link.objects.filter(link_category=category).all().order_by('-link_created')
	paginator = Paginator(links_list, 25)

	page = request.GET.get('page')

	try:
		links = paginator.page(page)
	except PageNotAnInteger:
		links = paginator.page(1)
	except EmptyPage:
		links = paginator.page(paginator.num_pages)

	return render(request, 'view_category.html', {
		'categories': Category.objects.all(),
		'category': category,
		'links': links
	})

def view_link(request, id):
	link = get_object_or_404(Link, pk=id)
	return render(request, 'view_link.html', {
		'link': link,
		'categories': Category.objects.all(),
	})

def redirect_link(request, id):
	link = get_object_or_404(Link, pk=id)
	return redirect(link.link_url)