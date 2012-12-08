from datetime import timedelta

class UnionAffiliation(object):
    def __init__(self, dues):
        self.dues = dues
        self.service_charges = {}

    def get_service_charge(self, date):
        return self.service_charges[date]

    def add_service_charge(self, date, service_charge):
        self.service_charges[date] = service_charge

    def calculate_deductions(self, paycheck):
        deductions = self.dues
        days = (paycheck.pay_date - paycheck.start_date).days
        print self.service_charges

        for days_offset in range(days+1):
            date = paycheck.start_date + timedelta(days_offset)
            try:
                deductions += self.get_service_charge(date).charge
            except KeyError:
                pass

        paycheck.deductions = deductions
