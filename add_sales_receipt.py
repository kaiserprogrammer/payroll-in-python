from sales_receipt import SalesReceipt

class AddSalesReceipt(object):
    def __init__(self, empId, date, amount, db):
        self.empId = empId
        self.date = date
        self.amount = amount
        self.db = db

    def execute(self):
        e = self.db.get_employee(self.empId)
        pc = e.classification
        pc.add_sales_receipt(SalesReceipt(self.date, self.amount))
