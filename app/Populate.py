from app.models import personel , complain , crew
from datetime import date, timedelta


class Populate(object):
    """docstring for Populate."""

    def __init__(self, arg):
        self.arg = arg


    def count_incid(self):
        count = []
        for i in range(1,13):
            count.append( complain.objects.filter( created__month = i).count())
        return str(count)

    def lastweek(self):
        send = {}
        count = []
        days = []
        today_date = date.today()
        sum = 0
        for i in range(1,8):
            forming = today_date.day - i
            #forming = str(forming) + '.' + str(today_date.month)
            days.append( forming )
            counter = complain.objects.filter( created__day = today_date.day -i  ).count()
            count.append(counter)
            sum = sum + counter
        send = { "days" : days , "count" : count , "sum" : sum}
        return send


    def lastweek_resolved(self):
        send = {}
        count = []
        days = []
        today_date = date.today()
        sum = 0
        for i in range(1,8):
            counter = complain.objects.filter( created__day = today_date.day -i , resolved=True).count()
            count.append(counter)
            sum = sum + counter
        send = { "days" : days , "count" : count , "sum" : sum}
        return send
