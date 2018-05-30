# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models, wordFinder
from django.views import View

import collections


class WordFinder(View):

    def get(self, request):
        context = {
            'wordform': models.WordForm(),
        }
        return render(request, 'wordfinder.html', context=context)

    def post(self, request):

        form = models.WordForm(request.POST)
        if form.is_valid():
            queryWord = form.clean().get('word')
            found = wordFinder.findWordinLibraryBinarySearch(queryWord)
            # found = wordFinder.linearSearch(queryWord)
            # found = wordFinder.findWordinLibraryStandard(queryWord)
            time = found['time']
            del found['time']
            print time

            found = collections.OrderedDict(sorted(found.items()))
            context = {
                'wordform': models.WordForm(),
                'words': found,
                'time': time,
            }

        return render(request, 'wordfinder.html', context=context)
