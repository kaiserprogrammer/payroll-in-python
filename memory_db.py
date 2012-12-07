class MemoryDB(object):
    def __init__(self):
        self.employees = {}
        self.id = 0

    def next_id(self):
        self.id += 1
        return self.id

    def get_employee(self, id):
        return self.employees[id]

    def add_employee(self, employee):
        employee.id = self.next_id()
        self.employees[employee.id] = employee

