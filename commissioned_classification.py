class CommissionedClassification(object):
    def __init__(self, commission, baseRate):
        self.commission = commission
        self.baseRate = baseRate
        self.sales_receipts = []

    def get_sales_receipts(self):
        return self.sales_receipts

    def add_sales_receipt(self, sale):
        self.sales_receipts.append(sale)

    def calculate_pay(self, paycheck):
        salary = self.baseRate
        for sale in self.sales_receipts:
            if sale.date >= paycheck.start_date and sale.date <= paycheck.pay_date:
                print salary
                salary += sale.amount * self.commission / 100

        paycheck.gross_pay = salary
