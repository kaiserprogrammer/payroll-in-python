from change_classification import ChangeClassification
from salaried_classification import SalariedClassification
from monthly_schedule import MonthlySchedule

class ChangeSalaried(ChangeClassification):
    def __init__(self, empId, salary, db):
        ChangeClassification.__init__(self, empId, db)
        self.salary = salary

    def make_classification(self, employee):
        pc = SalariedClassification(self.salary)
        employee.classification = pc

    def make_schedule(self, employee):
        employee.schedule = MonthlySchedule()
