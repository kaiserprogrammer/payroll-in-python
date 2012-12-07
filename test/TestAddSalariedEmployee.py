from memory_db import MemoryDB
from add_salaried_employee import AddSalariedEmployee
from salaried_classification import SalariedClassification
from monthly_schedule import MonthlySchedule
from hold_method import HoldMethod

def test_adding_an_employee_paid_by_salary():
    db = MemoryDB()
    t = AddSalariedEmployee("Jim", "Work", 2000.0, db)
    empId = t.execute()
    e = db.get_employee(empId)

    assert e.name, "Jim"
    assert e.address, "Work"

    pc = e.classification
    assert isinstance(pc, SalariedClassification)
    assert pc.salary == 2000.0

    ps = e.schedule
    assert isinstance(ps, MonthlySchedule)

    pm = e.method
    assert isinstance(pm, HoldMethod)
