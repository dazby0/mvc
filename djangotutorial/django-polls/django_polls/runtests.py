import os
import sys
import django
from django.conf import settings
from django.test.utils import get_runner

def runtests():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')
    
    if not settings.configured:
        settings.configure(
        DEBUG=True,
        SECRET_KEY='test-secret-key',
        USE_I18N=True,
        USE_L10N=True,
        USE_TZ=True,
        LANGUAGE_CODE='en-us',
        TIME_ZONE='UTC',
        ROOT_URLCONF='django_polls.tests.urls',
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django_polls',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        MIDDLEWARE=[],
    )

    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(['django_polls'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
