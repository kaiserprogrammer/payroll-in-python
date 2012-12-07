from memory_db import MemoryDB
from add_commissioned_employee import AddCommissionedEmployee
import datetime
from add_sales_receipt import AddSalesReceipt
from commissioned_classification import CommissionedClassification

def test_adding_a_sales_receipt():
    db = MemoryDB()
    t = AddCommissionedEmployee("John", "Home", 5.0, 1500, db)
    empId = t.execute()
    date = datetime.date(2005, 3, 30)
    srt = AddSalesReceipt(empId, date, 500, db)
    srt.execute()

    e = db.get_employee(empId)
    assert e is not None

    pc = e.classification
    assert isinstance(pc, CommissionedClassification)

    srs = pc.get_sales_receipts()
    assert srs[0].amount == 500
    assert srs[0].date == date
