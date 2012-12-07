from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
from change_name import ChangeName

def test_changing_name_of_an_employee():
    db = MemoryDB()
    empId = AddHourlyEmployee("wrong", "Home", 1, db).execute()

    cnt = ChangeName(empId, "Bill", db)
    cnt.execute()

    e = db.get_employee(empId)
    assert e.name == "Bill"
