class SalariedClassification(object):
    def __init__(self, salary):
        self.salary = salary

    def calculate_pay(self, paycheck):
        paycheck.gross_pay = self.salary
