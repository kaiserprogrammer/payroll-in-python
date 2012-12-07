from employee import Employee
from hold_method import HoldMethod

class AddEmployee(object):
    def __init__(self, name, address, db):
        self.name = name
        self.address = address
        self.db = db

    def execute(self):
        self.e = Employee(self.name, self.address)
        self.make_classification()
        self.make_schedule()
        self.e.method = HoldMethod()
        self.db.add_employee(self.e)
        return self.e.id


