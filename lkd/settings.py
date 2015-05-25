"""
Django settings for lkd project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!qa^6fp!n&pukb*qh)e6zl_y=)p&-mulj-dd=et9oqjt4_0-)8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PRODUCTION = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pytils',
    'paper',
    'link',
    'userprofile',
    'social_auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
                      #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'lkd.context_processors.site.main',
)

ROOT_URLCONF = 'lkd.urls'

WSGI_APPLICATION = 'lkd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Twitter 

TWITTER_ON = False

TWITTER_CONSUMER_KEY = 'puWNMd0SsPTlXYQmbZmY6VZ8i'

TWITTER_CONSUMER_SECRET = 'VGer8P0FDZWFQvLSUmHlPh2j4I6lfYIjaJpxWfQM0HgsOuCDt1'

TWITTER_ACCESS_TOKEN = '1945001869-Z6QB0kPzxa61HBUC9L3xQhOMTYIqTPbTSRRhwxM'

TWITTER_ACCESS_TOKEN_SECRET = 'Y62T11nW7RbOciNSwERsxBf6GpT7ngguNRU7BCtd4NKXf'

# Vkontakte

VK_ON = False

VK_APP_ID = '4655060'
VK_API_SECRET = 'i3i6EenLCpYnIEhB7Jti'

VKONTAKTE_APP_ID = '4655060'
VKONTAKTE_API_SECRET = 'i3i6EenLCpYnIEhB7Jti'

VK_APP_TOKEN = 'c00566288d41f3f7f26c429b8bc2e58ed120408e6ba7f8fb61311ca3ac3d6d2f2acd03868a3a634002894'
VK_APP_PUBLIC = -72915901

FACEBOOK_APP_ID = '330231353768030'
FACEBOOK_API_SECRET = 'f2b426ca1f5400f5e75f95da40af571e'

if PRODUCTION:
    GITHUB_APP_ID = 'e01fd8f29e9bf4a8cf99'
    GITHUB_API_SECRET = '248dad8c1c5f9489e63effbd5986d8a11cd10ffd'
else:
    GITHUB_APP_ID = 'b3f1ec85ad166ac038c2'
    GITHUB_API_SECRET = '812f3650edc8249597b82b0f095a5afa49ed9e05'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static-dev/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static-dev'),
)

STATIC_ROOT = '/static-prod/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.github.GithubBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_CREATE_USERS = True

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)

LOGIN_URL = '/login/github/'
LOGIN_REDIRECT_URL = '/'
LANGUAGE_CODE = 'ru-ru'
COMMENTS_APP = 'threadedcomments'
