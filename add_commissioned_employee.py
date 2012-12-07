from commissioned_classification import CommissionedClassification
from biweekly_schedule import BiWeeklySchedule
from add_employee import AddEmployee

class AddCommissionedEmployee(AddEmployee):
    def __init__(self, name, address, commission, baseRate, db):
        AddEmployee.__init__(self, name, address, db)
        self.commission = commission
        self.baseRate = baseRate

    def make_classification(self):
        self.e.classification = CommissionedClassification(self.commission, self.baseRate)

    def make_schedule(self):
        self.e.schedule = BiWeeklySchedule()
