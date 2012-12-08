class MonthlySchedule(object):
    def isPayday(self, date):
        try:
            date.replace(day=date.day+1)
            return False
        except ValueError:
            return True

    def get_pay_period_start_date(self, date):
        return date.replace(day=1)
