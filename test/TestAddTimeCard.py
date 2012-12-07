from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
import datetime
from add_time_card import AddTimeCard
from hourly_classification import HourlyClassification

def test_adding_a_time_card():
    db = MemoryDB()
    t = AddHourlyEmployee("Bill", "Home", 15.25, db)
    empId = t.execute()
    date = datetime.date(2005, 3, 30)
    tct = AddTimeCard(empId, date, 8.0, db)
    tct.execute()

    e = db.get_employee(empId)
    assert e is not None

    pc = e.classification
    assert isinstance(pc, HourlyClassification)

    tc = pc.get_time_card(date)
    assert tc.hours == 8.0
    assert tc.date == date
