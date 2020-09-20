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
        for i in range(1,8):
            forming = today_date.day - i
            #forming = str(forming) + '.' + str(today_date.month)
            days.append( forming )
            count.append(complain.objects.filter( created__day = today_date.day -i  ).count())
        send = { "days" : days , "count" : count}
        return send


    def lastweek_resolved(self):
        send = {}
        count = []
        days = []
        today_date = date.today()
        for i in range(1,8):
            count.append(complain.objects.filter( created__day = today_date.day -i , resolved=False).count())
        send = { "days" : days , "count" : count}
        return send
