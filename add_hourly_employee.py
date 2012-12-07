from add_employee import AddEmployee
from hourly_classification import HourlyClassification
from weekly_schedule import WeeklySchedule

class AddHourlyEmployee(AddEmployee):
    def __init__(self, name, address, rate, db):
        AddEmployee.__init__(self, name, address, db)
        self.rate = rate

    def make_classification(self):
        self.e.classification = HourlyClassification(self.rate)

    def make_schedule(self):
        self.e.schedule = WeeklySchedule()
