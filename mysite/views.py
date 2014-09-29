from django.shortcuts import render
from django.http import *
from models import Phrase
import re
from string import punctuation
from forms import DateForm


def index(request):
    return render(request, 'index.html')


def phrases_per_date(request):
    form = DateForm()
    selected_day = request.GET.get("day")
    selected_month = request.GET.get("month")
    matching_phrases = Phrase.objects.filter(day=selected_day, month=selected_month)

    return render(request, 'date_filter.html', {'form': form, 'matching_phrases': matching_phrases})


def word_count(request):
    phrases = Phrase.objects.all()
    r = re.compile(r'[{}]'.format(punctuation))

    html = '<html><head><title>Word count</title><body><h1>Word count per phrase</h1><ul>'

    for p in phrases:
        s = r.sub(' ', p.body)
        phrase_count = len(s.split())
        html += '<li>%s : %s</li>' % (p.title, phrase_count)

    html += '</ul></body></html>'

    return render(request, 'wordcount.html', {'phrases': phrases})


def rotations(request):
    phrases = Phrase.objects.all()

    def is_rotation(a, b):

        low_a = a.lower()
        low_b = b.lower()

        if len(a) != len(b):
            return False

        for x in range(len(a)):
            if low_b.startswith(low_a[x:]) and low_b.endswith(low_a[:x]):
                return True

        return False

    rotations = []

    for p in phrases:
        words = p.body.split(' ')

        # Split into subsets of two
        t = [words[n:n + 2] for n, i in enumerate(words) if n % 2 == 0]

        # check for rotations
        for subset in t:
            if len(subset) == 2 and is_rotation(subset[0], subset[1]):
                rotations.append(subset)

    return render(request, 'rotations.html', {'rotations': rotations})