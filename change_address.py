from change_employee import ChangeEmployee

class ChangeAddress(ChangeEmployee):
    def __init__(self, empId, address, db):
        ChangeEmployee.__init__(self, empId, db)
        self.address = address

    def change(self, employee):
        employee.address = self.address
