from django.contrib.auth.models import User
from link.models import Link, Category
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def view_user(request, id):

	profile = get_object_or_404(User, id=id)

	links_list = Link.objects.all().filter(link_author=profile.id)
	paginator = Paginator(links_list, 5)

	page = request.GET.get('page')

	try:
		links = paginator.page(page)
	except PageNotAnInteger:
		links = paginator.page(1)
	except EmptyPage:
		links = paginator.page(paginator.num_pages)

	return render(request, 'view_user.html', {
		'profile': profile,
		'links': links
	})