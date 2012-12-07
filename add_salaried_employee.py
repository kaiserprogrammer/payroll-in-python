from add_employee import AddEmployee
from monthly_schedule import MonthlySchedule
from salaried_classification import SalariedClassification

class AddSalariedEmployee(AddEmployee):
    def __init__(self, name, address, salary, db):
        AddEmployee.__init__(self, name, address, db)
        self.salary = salary

    def make_classification(self):
        self.e.classification = SalariedClassification(self.salary)

    def make_schedule(self):
        self.e.schedule = MonthlySchedule()
