from memory_db import MemoryDB
from add_commissioned_employee import AddCommissionedEmployee
from change_salaried import ChangeSalaried
from salaried_classification import SalariedClassification
from monthly_schedule import MonthlySchedule

def test_changing_an_employee_to_be_paid_by_commission():
    pass

def test_changing_an_address_of_an_employee():
    db = MemoryDB()
    empId = AddCommissionedEmployee("Bohn", "wrong", 1, 150, db).execute()

    cs = ChangeSalaried(empId, 1500, db)
    cs.execute()

    e = db.get_employee(empId)

    pc = e.classification
    assert isinstance(pc, SalariedClassification)
    assert pc.salary == 1500

    ps = e.schedule
    assert isinstance(ps, MonthlySchedule)
