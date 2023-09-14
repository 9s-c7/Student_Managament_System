# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from apps.home.models import Event

admin.site.register(Event)