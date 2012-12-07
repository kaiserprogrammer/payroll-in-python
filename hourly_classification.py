class HourlyClassification(object):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.time_cards = {}

    def get_time_card(self, date):
        return self.time_cards[date]

    def add_time_card(self, timecard):
        self.time_cards[timecard.date] = timecard

