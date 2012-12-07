class DeleteEmployee(object):
    def __init__(self, empId, db):
        self.empId = empId
        self.db = db

    def execute(self):
        self.db.remove_employee(self.empId)
