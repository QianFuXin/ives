# encoding:utf-8
import datetime
import time

import dateutil

style = "%Y%m%d %H:%M:%S"
now = time.strftime(style, time.localtime())
lastYear = (datetime.datetime.now() + dateutil.relativedelta.relativedelta(years=-1)).__format__(style)
lastMonth = (datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=-1)).__format__(style)
lastDay = (datetime.datetime.now() + dateutil.relativedelta.relativedelta(days=-1)).__format__(style)
lastHour = (datetime.datetime.now() + dateutil.relativedelta.relativedelta(hours=-1)).__format__(style)
lastMinute = (datetime.datetime.now() + dateutil.relativedelta.relativedelta(minutes=-1)).__format__(style)
lastSecond = (datetime.datetime.now() + dateutil.relativedelta.relativedelta(seconds=-1)).__format__(style)
