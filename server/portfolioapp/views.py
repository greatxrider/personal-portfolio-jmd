"""this is the views.py file for the djangoapp app"""""
import logging
import json
import random
import pdb
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

#index view
def index(request):
    """index page"""
    context = {}
    if request.method=='GET':
        return render(request, 'portfolioapp/index.html', context)
