class MemoryDB(object):
    def __init__(self):
        self.employees = {}
        self.members = {}
        self.id = 0

    def next_id(self):
        self.id += 1
        return self.id

    def get_employee(self, id):
        return self.employees[id]

    def add_employee(self, employee):
        employee.id = self.next_id()
        self.employees[employee.id] = employee

    def remove_employee(self, empId):
        self.employees.pop(empId)

    def add_union_member(self, member):
        member.memberId = self.next_id()
        self.members[member.memberId] = member

    def get_union_member(self, memberId):
        return self.members[memberId]

    def remove_union_member(self, memberId):
        self.members.pop(memberId)

    def get_all_employees(self):
        return self.employees.values()
