from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
from change_commissioned import ChangeCommissioned
from commissioned_classification import CommissionedClassification
from biweekly_schedule import BiWeeklySchedule

def test_changing_an_employee_to_be_paid_by_commission():
    pass

def test_changing_an_address_of_an_employee():
    db = MemoryDB()
    empId = AddHourlyEmployee("Bohn", "wrong", 1, db).execute()

    cc = ChangeCommissioned(empId, 2.5, 1000, db)
    cc.execute()

    e = db.get_employee(empId)

    pc = e.classification
    assert isinstance(pc, CommissionedClassification)
    assert pc.baseRate == 1000
    assert pc.commission == 2.5

    ps = e.schedule
    assert isinstance(ps, BiWeeklySchedule)
