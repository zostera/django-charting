import django.conf.global_settings as DEFAULT_SETTINGS


SECRET_KEY = 'django-charting-test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'charting',
)

MIDDLEWARE_CLASSES = DEFAULT_SETTINGS.MIDDLEWARE_CLASSES

CHARTING = {
}
