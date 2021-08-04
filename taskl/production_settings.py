import os

LOGIN_URL = 'https://taskl.app/login' #TODO: change to use ssl for prod
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['TASKL_EMAIL_HOST']
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['TASKL_EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['TASKL_EMAIL_HOST_PASSWORD']

CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True