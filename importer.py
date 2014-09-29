import sys,os

sys.path.extend(['/Users/manuel/Development/prueba/'])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from mysite.models import Phrase
import csv


# Full path to phrase file
file = "lynxoft-test.tab"

reader = csv.reader(open(file), delimiter=',', quotechar='"')

for line in reader:

    # Skip header row
    if line[0] != 'title':

        p = Phrase()

        if line[0] is not None:
            p.title = line[0]

        if line[1] is not None:
            p.month = line[1]

        if line[2] is not None:
            p.day = line[2]

        if line[3] is not None:
            p.body = line[3]

        p.save()


