import datetime

class HourlyClassification(object):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.time_cards = {}

    def get_time_card(self, date):
        return self.time_cards[date]

    def add_time_card(self, timecard):
        self.time_cards[timecard.date] = timecard

    def calculate_pay(self, paycheck):
        salary = 0
        for days_offset in range(0, 14):
            date = paycheck.start_date + datetime.timedelta(days=days_offset)
            try:
                tc = self.get_time_card(date)
                salary += tc.hours * self.hourly_rate
                if tc.hours > 8:
                    salary += (tc.hours - 8) / 2 * self.hourly_rate
            except KeyError:
                pass
        paycheck.gross_pay = salary
