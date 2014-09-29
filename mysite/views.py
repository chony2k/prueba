from django.http import HttpResponse
from models import Phrase
import re
from string import punctuation

def word_count(request):

   phrases = Phrase.objects.all()
   r = re.compile(r'[{}]'.format(punctuation))

   html = '<html><head><title>Word count</title><body><h1>Word count per phrase</h1><ul>'

   for p in phrases:
        s = r.sub(' ',  p.body)
        phrase_count = len(s.split())
        html += '<li>%s : %s</li>' % (p.title, phrase_count)

   html += '</ul></body></html>'


   return HttpResponse(html)