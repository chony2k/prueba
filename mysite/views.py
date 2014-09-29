#coding=UTF-8

from django.shortcuts import render
from django.http import *
from models import Phrase
from forms import DateForm


def index(request):
    """
    Default view
    """
    return render(request, 'index.html')


def phrases_per_date(request):
    """
    Filters the phrases so only the ones with the specified day and month are returned.
    The parameters are passed by GET for brevity and simplicity.
    TODO: Do some error checking and validation
    """

    def is_number(s):
        """
        Checks if a string can be converted to an integer
        """
        if s is None:
            return False
        try:
            int(s)
            return True
        except ValueError:
            return False

    form = DateForm()

    selected_day = request.GET.get("day")
    selected_month = request.GET.get("month")

    if is_number(selected_day) and is_number(selected_month):
        matching_phrases = Phrase.objects.filter(day=selected_day, month=selected_month)
    else:
        matching_phrases = Phrase.objects.all()

    return render(request, 'date_filter.html', {'form': form, 'matching_phrases': matching_phrases})


def word_count(request):
    """
    Displays a list with phrase title followed by the word count in the body of each
    The filter wordcount is used to count the words
    """
    phrases = Phrase.objects.all()
    return render(request, 'wordcount.html', {'phrases': phrases})


def rotations(request):
    """
    Displays a list of words which are rotations of the same string. The search is performed in the body field
    of each phrase
    """
    phrases = Phrase.objects.all()

    def is_rotation(a, b):
        """
        Returns if string "a" is rotation of "b" or viceversa.
        The method works by checking if either string A or B starts or ends with the other, inside a loop,
        so that each possible combination is tested
        """

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