# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse


# Create your views here.


def login(request):
    return render(request, 'login.html')


def home(request):
    print request
    return HttpResponseRedirect(reverse('taskpop:login'))