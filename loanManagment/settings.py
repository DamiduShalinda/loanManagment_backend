
from pathlib import Path
import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f8n2)q&yjnk7!l40*8(-_k-tk2(z($_mymf3#a(2v^*5t$v&7)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'cloudinary' ,
    'cloudinary_storage' ,
    
    'users',
    'StaffProfile',
    'CustomerProfile',
    'loans',
    'loanvalues',
    'loanarrears',
    'analytics',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'loanManagment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'loanManagment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'hasaru_db',  
        'USER': 'root',  
        'PASSWORD': 'root',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }  
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Colombo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

ALLOWED_HOSTS = [
    '10.0.2.2', 
    'localhost', 
    '127.0.0.1' , 
    'rarely-worthy-gopher.ngrok-free.app'
    ]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
    'http://rarely-worthy-gopher.ngrok-free.app'
    # Add other trusted origins if needed
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'damidushalinda10@gmail.com'
EMAIL_HOST_PASSWORD = 'mlxlylgojphgyifr'

          
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dfvhftecz',
    'API_KEY' : '454366385488942' ,
    'API_SECRET' : '0shsAbsyZMqv5xgbcml8FCM48sQ'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

import cloudinary

cloudinary.config( 
  cloud_name = "dfvhftecz", 
  api_key = "454366385488942", 
  api_secret = "0shsAbsyZMqv5xgbcml8FCM48sQ" 
)


JAZZMIN_SETTINGS = {
    "site_title": "Hasaru Enterprises",
    "site_header": "Admin",
    "site_brand": "Hasaru Enterprises",
    "welcome_sign": "Welcome Back !!",
    "search_model": ["Loans.loan_number", "CustomerProfile.name"],
    "hide_models": ['auth.Group'],
    "order_with_respect_to": ["Loans", "CustomerProfile" ,  "loanvalues" , "loanarrears" , "analytics", "StaffProfile" ,],
    
    
}
