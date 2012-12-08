import datetime

class BiWeeklySchedule(object):
    def isPayday(self, date):
        if date.isoweekday() == 5:
            return date.isocalendar()[1] % 2 == 0
        else:
            return False

    def get_pay_period_start_date(self, date):
        return date - datetime.timedelta(days=13)
