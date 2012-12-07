from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
from hourly_classification import HourlyClassification
from weekly_schedule import WeeklySchedule
from hold_method import HoldMethod

def test_adding_an_hourly_paid_employee():
    db = MemoryDB()
    at = AddHourlyEmployee("John", "Home", 15.75, db)
    empId = at.execute()
    e = db.get_employee(empId)

    assert e is not None
    assert e.id == empId
    assert e.name == "John"
    assert e.address == "Home"
    pc = e.classification
    assert isinstance(pc, HourlyClassification)
    assert pc.hourly_rate == 15.75
    ps = e.schedule
    assert isinstance(ps, WeeklySchedule)
    pm = e.method
    assert isinstance(pm, HoldMethod)
