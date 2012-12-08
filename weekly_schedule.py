import datetime

class WeeklySchedule(object):
    def isPayday(self, date):
        if (date.isoweekday() == 5):
            return True
        else:
            return False

    def get_pay_period_start_date(self, date):
        return date - datetime.timedelta(days=7)
