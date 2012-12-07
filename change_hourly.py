from change_classification import ChangeClassification
from hourly_classification import HourlyClassification
from weekly_schedule import WeeklySchedule

class ChangeHourly(ChangeClassification):
    def __init__(self, empId, rate, db):
        ChangeClassification.__init__(self, empId, db)
        self.rate = rate

    def make_classification(self, employee):
        employee.classification = HourlyClassification(self.rate)

    def make_schedule(self, employee):
        employee.schedule = WeeklySchedule()
