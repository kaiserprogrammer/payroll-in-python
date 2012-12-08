from no_affiliation import NoAffiliation

class Employee(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.affiliation = NoAffiliation()

    def isPayday(self, date):
        return self.schedule.isPayday(date)

    def get_pay_period_start_date(self, date):
        return self.schedule.get_pay_period_start_date(date)

    def payday(self, paycheck):
        self.classification.calculate_pay(paycheck)
        self.affiliation.calculate_deductions(paycheck)
        self.method.disposition(paycheck)
        paycheck.net_pay = paycheck.gross_pay - paycheck.deductions
