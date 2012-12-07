class ChangeEmployee(object):
    def __init__(self, empId, db):
        self.empId = empId
        self.db = db

    def execute(self):
        e = self.db.get_employee(self.empId)
        self.change(e)
