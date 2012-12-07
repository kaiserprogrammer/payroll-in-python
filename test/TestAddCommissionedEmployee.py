from memory_db import MemoryDB
from add_commissioned_employee import AddCommissionedEmployee
from commissioned_classification import CommissionedClassification
from biweekly_schedule import BiWeeklySchedule
from hold_method import HoldMethod

def test_adding_an_employee_paid_by_commission():
    db = MemoryDB()
    t = AddCommissionedEmployee("Sorro", "Firm", 5.0, 1000, db)
    empId = t.execute()

    e = db.get_employee(empId)
    assert e.name == "Sorro"
    assert e.address == "Firm"

    pc = e.classification
    assert isinstance(pc, CommissionedClassification)
    assert pc.commission == 5.0
    assert pc.baseRate == 1000

    ps = e.schedule
    assert isinstance(ps, BiWeeklySchedule)

    pm = e.method
    assert isinstance(pm, HoldMethod)
