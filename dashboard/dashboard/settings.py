from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-z&*fm=ep=x@_a9cme5u!p)zx904fhdss77gvdftd+kl8roq-0s'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard_app', 
    'frontend', 
    'adminlte3',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add directories where your templates are stored
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dashboard.wsgi.application'

# Database configuration (SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'dashboard', 
        'USER':'root',
        'PASSWORD':'Vijay123',
        'HOST':'localhost',
        'PORT': '3306'

          # SQLite database file located in your project directory
    }
}



# Password validation (Django's default)
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
# settings.py

# Other settings...

# settings.py

STATIC_URL = '/static/'

# Directories where Django will look for static files
STATICFILES_DIRS = [
    BASE_DIR / 'dashboard_app' / 'static',  # Your app's static folder
    BASE_DIR / 'frontend' / 'static',  # Additional static folder from frontend if needed
]

STATIC_ROOT = BASE_DIR / 'staticfiles'  # Folder for collected static files



# Login settings
LOGIN_URL = 'login'  # Redirect to this URL if user is not logged in
LOGIN_REDIRECT_URL = 'indexpage'  # Redirect after successful login
LOGOUT_REDIRECT_URL = '/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

