from change_employee import ChangeEmployee

class ChangeClassification(ChangeEmployee):
    def __init__(self, empId, db):
        ChangeEmployee.__init__(self, empId, db)

    def change(self, employee):
        self.make_classification(employee)
        self.make_schedule(employee)
