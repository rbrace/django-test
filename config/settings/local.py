from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='0j=^hh2ehem36vg7l%j7g^1)d(h=s2na2#z6=812l^95+%wify')

DEBUG = env.bool('DJANGO_DEBUG', default=True)


