from change_classification import ChangeClassification
from commissioned_classification import CommissionedClassification
from biweekly_schedule import BiWeeklySchedule

class ChangeCommissioned(ChangeClassification):
    def __init__(self, empId, commission, baseRate, db):
        ChangeClassification.__init__(self, empId, db)
        self.commission = commission
        self.baseRate = baseRate

    def make_classification(self, employee):
        pc = CommissionedClassification(self.commission, self.baseRate)
        employee.classification = pc

    def make_schedule(self, employee):
        employee.schedule = BiWeeklySchedule()
