from time_card import TimeCard

class AddTimeCard(object):
    def __init__(self, empId, date, hours, db):
        self.empId = empId
        self.date = date
        self.hours = hours
        self.db = db

    def execute(self):
        e = self.db.get_employee(self.empId)
        pc = e.classification
        tc = TimeCard(self.date, self.hours)
        pc.add_time_card(tc)
