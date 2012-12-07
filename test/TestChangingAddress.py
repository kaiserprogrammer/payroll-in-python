from memory_db import MemoryDB
from add_hourly_employee import AddHourlyEmployee
from change_address import ChangeAddress

def test_changing_an_address_of_an_employee():
    db = MemoryDB()
    empId = AddHourlyEmployee("Bohn", "wrong", 1, db).execute()

    cat = ChangeAddress(empId, "Home", db)
    cat.execute()

    e = db.get_employee(empId)
    assert e is not None
    assert e.address == "Home"
