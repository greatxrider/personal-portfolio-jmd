"""this is the models.py file for the djangoapp app"""
import sys
from django.utils.timezone import now
from django.conf import settings
try:
    from django.db import models
except Exception:
    print("There was an error loading django modules. Do you have django installed?")
    sys.exit()
