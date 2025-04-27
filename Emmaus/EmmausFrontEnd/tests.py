from django.test import TestCase
import datetime
from datetime import datetime, timedelta
from pytz import timezone


# Create your tests here.
#print (datetime.datetime.now() - datetime.timedelta(hours=4)).strftime("%B %d, %Y %Z%z")
eastern = timezone('US/Eastern')
fmt = '%Y'
loc_dt = eastern.localize(datetime.now()) - timedelta(hours=4)
print (loc_dt.strftime(fmt))