from django.core.context_processors import request

def main(request):
	return {
		'SITE_URL': 'Lkd.to',
		'SITE_VK_URL': 'https://vk.com/lkdto',
		'SITE_TW_URL': 'https://twitter.com/lkd_to'
	}