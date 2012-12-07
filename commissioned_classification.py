class CommissionedClassification(object):
    def __init__(self, commission, baseRate):
        self.commission = commission
        self.baseRate = baseRate
        self.sales_receipts = []

    def get_sales_receipts(self):
        return self.sales_receipts

    def add_sales_receipt(self, sale):
        self.sales_receipts.append(sale)
