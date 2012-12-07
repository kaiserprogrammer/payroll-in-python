from change_employee import ChangeEmployee

class ChangeName(ChangeEmployee):
    def __init__(self, empId, name, db):
        ChangeEmployee.__init__(self, empId, db)
        self.name = name

    def change(self, employee):
        employee.name = self.name
