from app.models import personel , complain , crew, infrastructure
from datetime import date, timedelta
from django.db.models.functions import ExtractMonth
import datetime


class Populate(object):
    """docstring for Populate."""

    def __init__(self, arg):
        self.arg = arg


    def count_incid(self):
        count = []
        for i in range(1,13):
            count.append( complain.objects.filter( created__month = i).count())
        return str(count)


    def perMonthIncidents(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        for entry in allComplains:
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[complainMonth] += 1
                    break
                i += 1
        return answer




    def perTypeFailPos(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        final = answer
        k = 0
        for value in answer:
            value = float(value * float(100/counter))
            final[k] = value
            k += 1
        return answer



    def perTypeIncidents(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        return answer

    def perMonthCosts(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        costs = [10, 40, 80, 30, 200, 120, 100, 140, 300, 180, 100]
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        for entry in allComplains:
            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[complainMonth] += costs[i]
                    break
                i += 1
        return answer






    def curMonthIncidents(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        for entry in allComplains:
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[complainMonth] += 1
                    break
                i += 1
        datee = datetime.datetime.now()
        curM = datee.month - 1
        return answer[curM]






    def curMonthType(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        datee = datetime.datetime.now()
        curM = datee.month
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            if entry.created.month == curM:
                counter += 1
                #m = str(entry.annotate(created__month = ExtractMonth()))

                infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
                findinf = infrastructure.objects.all().filter(UUID = infID)
                type = ''
                for result in findinf:
                    type = result.type
                complainMonth = entry.created.month -1
                i = 0
                for dt in damageTypes:
                    if type == dt:
                        answer[i] += 1
                        break
                    i += 1
        toreturn = [0 , '']
        for i in range (len(damageTypes)):
            if toreturn[0] < answer[i]:
                toreturn[0] = answer[i]
                toreturn[1] = damageTypes[i]
        return toreturn[1]




    def curMonthCost(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        costs = [10, 40, 80, 30, 200, 120, 100, 140, 300, 180, 100]
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        for entry in allComplains:
            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[complainMonth] += costs[i]
                    break
                i += 1
        datee = datetime.datetime.now()
        curM = datee.month - 1
        return answer[curM]




    def successfulRepairs(self):
        allComplains = complain.objects.all().filter(resolved = True)
        counter = 0
        for entry in allComplains:
            counter += 1
        return counter





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






















    def perTypeAlerts1(self):

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        first, second, third = [0, ''], [0, ''], [0, '']
        for i in range(len(damageTypes)):
            if first[0] < answer[i] :
                third[0], second[0], first[0] = second[0], first[0], answer[i]
                third[1], second[1], first[1] = second[1], first[1], damageTypes[i]
            elif second[0] < answer[i]:
                third[0], second[0] = second[0],  answer[i]
                third[1], second[1] = second[1],  damageTypes[i]
            elif third[0] < answer[i]:
                third[0] = answer[i]
                third[1] = damageTypes[i]
        toreturn = [first[0], first[1], second[0], second[1], third[0], third[1]]
        return first[0]

    def perTypeAlerts2(self):

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        first, second, third = [0, ''], [0, ''], [0, '']
        for i in range(len(damageTypes)):
            if first[0] < answer[i] :
                third[0], second[0], first[0] = second[0], first[0], answer[i]
                third[1], second[1], first[1] = second[1], first[1], damageTypes[i]
            elif second[0] < answer[i]:
                third[0], second[0] = second[0],  answer[i]
                third[1], second[1] = second[1],  damageTypes[i]
            elif third[0] < answer[i]:
                third[0] = answer[i]
                third[1] = damageTypes[i]
        toreturn = [first[0], first[1], second[0], second[1], third[0], third[1]]
        return first[1]


    def perTypeAlerts3(self):

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        first, second, third = [0, ''], [0, ''], [0, '']
        for i in range(len(damageTypes)):
            if first[0] < answer[i] :
                third[0], second[0], first[0] = second[0], first[0], answer[i]
                third[1], second[1], first[1] = second[1], first[1], damageTypes[i]
            elif second[0] < answer[i]:
                third[0], second[0] = second[0],  answer[i]
                third[1], second[1] = second[1],  damageTypes[i]
            elif third[0] < answer[i]:
                third[0] = answer[i]
                third[1] = damageTypes[i]
        toreturn = [first[0], first[1], second[0], second[1], third[0], third[1]]
        return second[0]



    def perTypeAlerts4(self):

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        first, second, third = [0, ''], [0, ''], [0, '']
        for i in range(len(damageTypes)):
            if first[0] < answer[i] :
                third[0], second[0], first[0] = second[0], first[0], answer[i]
                third[1], second[1], first[1] = second[1], first[1], damageTypes[i]
            elif second[0] < answer[i]:
                third[0], second[0] = second[0],  answer[i]
                third[1], second[1] = second[1],  damageTypes[i]
            elif third[0] < answer[i]:
                third[0] = answer[i]
                third[1] = damageTypes[i]
        toreturn = [first[0], first[1], second[0], second[1], third[0], third[1]]
        return second[1]


    def perTypeAlerts5(self):

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        first, second, third = [0, ''], [0, ''], [0, '']
        for i in range(len(damageTypes)):
            if first[0] < answer[i] :
                third[0], second[0], first[0] = second[0], first[0], answer[i]
                third[1], second[1], first[1] = second[1], first[1], damageTypes[i]
            elif second[0] < answer[i]:
                third[0], second[0] = second[0],  answer[i]
                third[1], second[1] = second[1],  damageTypes[i]
            elif third[0] < answer[i]:
                third[0] = answer[i]
                third[1] = damageTypes[i]
        toreturn = [first[0], first[1], second[0], second[1], third[0], third[1]]
        return third[0]



    def perTypeAlerts6(self):

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
        damageTypes = ['lamp', 'bench', 'pillar', 'road', 'theater', 'fountain', 'sidewalk', 'broken tank', 'hydrant', 'fallen tree', 'other']
        answer = [0 for i in range (12)]
        allComplains = complain.objects.all()
        counter = 0
        for entry in allComplains:
            counter += 1
            #m = str(entry.annotate(created__month = ExtractMonth()))

            infID = str(entry.infrastructure_id).replace('infrastructure object (' , '').replace(')', '')
            findinf = infrastructure.objects.all().filter(UUID = infID)
            type = ''
            for result in findinf:
                type = result.type
            complainMonth = entry.created.month -1
            i = 0
            for dt in damageTypes:
                if type == dt:
                    answer[i] += 1
                    break
                i += 1
        first, second, third = [0, ''], [0, ''], [0, '']
        for i in range(len(damageTypes)):
            if first[0] < answer[i] :
                third[0], second[0], first[0] = second[0], first[0], answer[i]
                third[1], second[1], first[1] = second[1], first[1], damageTypes[i]
            elif second[0] < answer[i]:
                third[0], second[0] = second[0],  answer[i]
                third[1], second[1] = second[1],  damageTypes[i]
            elif third[0] < answer[i]:
                third[0] = answer[i]
                third[1] = damageTypes[i]
        toreturn = [first[0], first[1], second[0], second[1], third[0], third[1]]
        return third[1]
