# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models, wordFinder
from django.views import View


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

            context = {
                'wordform': models.WordForm(),
                'words': found,
            }

        return render(request, 'wordfinder.html', context=context)
