from memory_db import MemoryDB
from add_salaried_employee import AddSalariedEmployee
from change_hourly import ChangeHourly
from hourly_classification import HourlyClassification
from weekly_schedule import WeeklySchedule

def test_changing_an_employee_to_be_paid_by_commission():
    pass

def test_changing_an_address_of_an_employee():
    db = MemoryDB()
    empId = AddSalariedEmployee("Bohn", "wrong", 1500, db).execute()

    cs = ChangeHourly(empId, 12.25, db)
    cs.execute()

    e = db.get_employee(empId)

    pc = e.classification
    assert isinstance(pc, HourlyClassification)
    assert pc.hourly_rate == 12.25

    ps = e.schedule
    assert isinstance(ps, WeeklySchedule)
