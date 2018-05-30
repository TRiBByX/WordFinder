# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms


class WordForm(forms.Form):
    word = forms.CharField(max_length=10)
