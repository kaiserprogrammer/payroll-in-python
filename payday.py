from paycheck import Paycheck

class Payday(object):
    def __init__(self, date, db):
        self.date = date
        self.db = db
        self.paychecks = {}

    def execute(self):
        for e in self.db.get_all_employees():
            if (e.isPayday(self.date)):
                start_date = e.get_pay_period_start_date(self.date)
                pc = Paycheck(start_date, self.date)
                self.paychecks[e.id] = pc
                e.payday(pc)

    def get_paycheck(self, empId):
        return self.paychecks[empId]
